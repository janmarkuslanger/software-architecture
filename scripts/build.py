"""Render src/topics into docs/ with citations resolved, then write README.md.

Topics cite sources by key ([@bass2021]). Pandoc resolves those keys against
references.bib in APA 7 style and appends the reference list under its own
heading, so no topic writes a reference list by hand.
"""

import re
import shutil
import subprocess
from collections.abc import Iterator
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "topics"
OUT = ROOT / "docs" / "topics"
INDEX = "index.md"
BIBLIOGRAPHY = ROOT / "references.bib"
CSL = ROOT / "scripts" / "apa.csl"
README = ROOT / "README.md"
README_TEMPLATE = ROOT / "src" / "readme.md"
TOPICS_PLACEHOLDER = "{{topics}}"

SOURCES_TITLE = "Sources"

PANDOC = [
    "pandoc",
    "--citeproc",
    "--fail-if-warnings",
    f"--bibliography={BIBLIOGRAPHY}",
    f"--csl={CSL}",
    "--metadata", f"reference-section-title={SOURCES_TITLE}",
    "--from", "markdown-smart",
    "--to", "gfm",
    "--wrap=preserve",
]

OWN_SOURCES_HEADING = re.compile(rf"^#+ {SOURCES_TITLE}$", re.MULTILINE)
GENERATED_SOURCES_HEADING = re.compile(rf"^# {SOURCES_TITLE}$", re.MULTILINE)


class BuildError(Exception):
    """Anything that makes the build unable to produce correct output."""


def docs_path(source: Path) -> Path:
    """Where a topic's rendered output lives. The only src-to-docs mapping."""
    return OUT / source.relative_to(SRC)


def shorten_rules(text: str) -> str:
    """Undo the padding pandoc adds to a horizontal rule."""
    return re.sub(r"^-{4,}$", "---", text, flags=re.MULTILINE)


def demote_sources_heading(text: str) -> str:
    """Put the reference section at level 2, behind a rule.

    Citeproc can only emit its heading at level 1 and has no option for this.
    """
    return GENERATED_SOURCES_HEADING.sub(f"---\n\n## {SOURCES_TITLE}", text)


def drop_div_wrappers(text: str) -> str:
    """Remove the <div>s around the reference list.

    They only carry CSS classes, and GitHub strips the stylesheet that would
    make them render any differently.
    """
    divs = ("<div", "</div>")
    return "\n".join(line for line in text.splitlines() if not line.startswith(divs))


def collapse_blank_runs(text: str) -> str:
    """Close the gaps left behind by the removed <div> lines."""
    return re.sub(r"\n{3,}", "\n\n", text)


def format_markdown(text: str) -> str:
    """Make pandoc's gfm output read like the hand-written source around it."""
    steps = (
        shorten_rules,
        demote_sources_heading,
        drop_div_wrappers,
        collapse_blank_runs,
    )

    for step in steps:
        text = step(text)

    return text


def require_no_sources_heading(source: Path, text: str) -> None:
    if OWN_SOURCES_HEADING.search(text):
        raise BuildError(
            f"{source}: remove the '{SOURCES_TITLE}' heading, the build adds it"
        )


def run_pandoc(source: Path, text: str) -> str:
    """Resolve the citation keys in one topic. Pandoc fails on an unknown key."""
    result = subprocess.run(
        PANDOC, input=text, capture_output=True, text=True, check=False
    )

    if result.returncode != 0:
        raise BuildError(f"{source}:\n{result.stderr.strip()}")

    return result.stdout


def title_of(source: Path, text: str) -> str:
    """Read a topic's title from its '# ' headline."""
    for line in text.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()

    raise BuildError(f"{source} has no '# ' headline")


def walk_topics(directory: Path, level: int = 0) -> Iterator[tuple[int, Path]]:
    """Yield every topic under directory, each parent directly above its children."""
    for child in sorted(p for p in directory.iterdir() if p.is_dir()):
        index = child / INDEX

        if index.exists():
            yield level, index
            yield from walk_topics(child, level + 1)


def topic_tree() -> str:
    """Render the topics in src/ as a nested markdown list linking into docs/."""
    lines = []

    for level, source in walk_topics(SRC):
        title = title_of(source, source.read_text(encoding="utf-8"))
        link = docs_path(source).relative_to(ROOT)
        lines.append("  " * level + f"- [{title}]({link})")

    return "\n".join(lines)


def render_topics() -> list[Path]:
    """Rebuild docs/ from src/. Returns the topics that were rendered."""
    if OUT.exists():
        shutil.rmtree(OUT)

    sources = sorted(SRC.rglob(INDEX))

    for source in sources:
        text = source.read_text(encoding="utf-8")
        require_no_sources_heading(source, text)

        target = docs_path(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(format_markdown(run_pandoc(source, text)), encoding="utf-8")

    return sources


def write_readme() -> None:
    """Fill the topics placeholder in the README template.

    Reads titles from src/ only, so this does not depend on docs/ having been
    rendered first.
    """
    template = README_TEMPLATE.read_text(encoding="utf-8")
    filled = template.replace(TOPICS_PLACEHOLDER, topic_tree())

    README.write_text(filled, encoding="utf-8")


def main() -> None:
    try:
        topics = render_topics()
        write_readme()
    except BuildError as error:
        raise SystemExit(f"build failed: {error}") from error

    print(f"rendered {len(topics)} topic(s) to docs/, wrote README.md")


if __name__ == "__main__":
    main()
