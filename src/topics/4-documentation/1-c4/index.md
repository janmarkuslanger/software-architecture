# C4

The C4 model consists of:

- Four hierarchical abstractions: software systems, containers, components and code [@brown2026, chap. 2]
- Four hierarchical diagrams: system context, containers, components and code [@brown2026, chap. 2]
- Three supporting diagrams: system landscape, dynamic and deployment [@brown2026, chap. 2, "Supporting Diagrams" section]

C4 is notation agnostic [@brown2026, chap. 2, "Notation" section] and tool agnostic [@brownc4model].

## Abstractions

### Software systems

A software system is something that delivers value to its users and is mostly developed by one team [@brown2026, chap. 2, "Software System" section].

### Containers

A container is a runnable unit. It is either an application or a data store [@brown2026, chap. 2, "Container" section].

### Components

A component groups related functionality inside a container with well-defined interfaces [@brown2026, chap. 2, "Component" section].

### Code

Code consists of the building blocks of the programming language like classes, interfaces or functions [@brown2026, chap. 2, "Code" section].

## Core diagrams

- [System Context Diagram](1-system-context/index.md)
- [Container Diagram](2-container/index.md)
- [Component Diagram](3-component/index.md)
- [Code Diagram](4-code/index.md)

## Supporting diagrams
- [System Landscape Diagram](5-system-landscape/index.md)
- [Dynamic Diagram](6-dynamic/index.md)
- [Deployment Diagram](7-deployment/index.md)

## Notation 

The C4 model is "notation independent" [@brown2026, chap. 10]. This means it is possible to choose existing notations like UML or create new ones [@brown2026, chap. 10]. The C4 model defines best practises for a good notation: notations make diagrams accessible and understandable, notation should be explained via a legend, and the notation is consistent in a diagram set [@brown2026, chap. 10, "What Makes a Good Notation?" section]. 

To achieve these characteristics, the C4 model gives the following best practises [@brown2026, chap. 10]:

- Diagrams should have titles with the diagram type (e.g. Container View) and the scope (e.g. Backend Tracking Service) [@brown2026, chap. 10, "Diagram Titles" section]. 

- "Incomprehensible acronyms, abbreviations, and code names can break an otherwise perfect diagram" [@brown2026, chap. 10, "Acronyms, Abbreviations, and Code Names" section]. Therefore they should be avoided, except for technical terms that are common in the current context (e.g. HTTP). If they are needed, they should be explained in a glossary or in the diagram key [@brown2026, chap. 10, "Acronyms, Abbreviations, and Code Names" section].

- There are no static layout rules, but the orientation should be consistent across the C4 levels, e.g. people always at the bottom [@brown2026, chap. 10, "Layout" section]. 

- Elements should contain information about their name (e.g. Backend Service), type (e.g. Container), technology for containers and components (e.g. Java) and a short description (e.g. handles tracking data). Shapes, colors and version numbers are optional and can be added to provide more information [@brown2026, chap. 10, "Elements" section].

- Relationships should be unidirectional, pointing from the initiating to the receiving element (e.g. Frontend makes API requests to Backend, the response is implied). Two arrows are only used if the relationships differ in intent, technology or synchronicity (e.g. Service A requests data from Service B, Service B publishes events to Service A). Labels should be specific (avoid words like "uses") and read like a sentence. Line styles, colors and arrowheads are optional [@brown2026, chap. 10, "Relationships" section].

- A diagram key should be added on or near the diagram to explain the notation used to differentiate elements and relationships (e.g. shapes, colors, icons, line styles) [@brown2026, chap. 10, "Diagram Key" section].