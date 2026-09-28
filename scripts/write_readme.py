from dataclasses import dataclass
from pathlib import Path

@dataclass
class Topic:
    path: str
    title: str

def extract_headline_from_markdown_file(path: str) -> str|None:
    with open(path) as file:
        for line in file:
            if line.strip().startswith("# "):
                return line.removeprefix("# ").strip()
            
def collect_topics() -> list[Topic]:
    topics = []
    directory = Path("./topics")
    
    for file in directory.rglob("*.md"):
        headline = extract_headline_from_markdown_file(file)
        topics.append(Topic(path=file, title=headline))
        
    return topics
            
def write_readme(topics: list[Topic]):
    content = ""
    
    with open("templates/readme.md") as file:
        content = file.read()
        
    topic_content = ""
    
    for topic in topics:
        topic_content += f"## [{topic.title}]({topic.path})\n\n"
    
    Path("README.md").write_text(content.replace("{{topics}}", topic_content), encoding="utf-8")    
    

def main():
    topics = collect_topics()
    write_readme(topics)
    
    
if __name__ == "__main__":
    main()