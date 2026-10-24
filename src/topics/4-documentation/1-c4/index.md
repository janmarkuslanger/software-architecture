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

---

## System Context Diagram

A system context diagram shows a software system with people and software systems interacting with it in a high-level view [@brown2026, chap. 3].

### What
A single software system with people and software systems that interact with it [@brown2026, chap. 3]

### Audience 
Technical and non technical people, everybody involved in the project [@brown2026, chap. 3]

### Content 

Software systems, people and relationships [@brown2026, chap. 3, "Content" section]

#### People

People who are using the system (prefered from a functional perspective) labeled with a name and a description [@brown2026, chap. 3, "People" section].


#### Software systems

The software system that is described and the software systems that interact with it. Every software system, should be labeled with a name and a description [@brown2026, chap. 3, "Software systems" section].

#### Relationships

Relationships should be created as "unidirectional arrows, each labeled with a summary of the relationship" [@brown2026, chap. 3, "Relationships" section]. 

### Example

```mermaid
C4Context
    Person(athlete, "Athlete", "Records workouts and views statistics")
    System(app, "Sports App", "Lets athletes track their workouts")
    System_Ext(tracker, "Fitness Tracker Platform", "Provides activity data recorded by wearables")

    Rel(athlete, app, "Records workouts and views statistics using")
    Rel(app, tracker, "Imports activity data from")

    UpdateLayoutConfig($c4ShapeInRow="1")
```

## Container Diagram

A container diagram shows the containers of a single software system [@brown2026, chap. 4].

### What

Containers of a single software system [@brown2026, chap. 4].

### Audience 

Software architects and engineers [@brown2026, chap. 4, "Audience" section]

### Content

#### People

People who are using a container of the software system (prefered from a functional perspective) labeled with a name and a description [@brown2026, chap. 4, "People and software systems" section].

#### Software Systems

The software systems that interact with a container of the software system [@brown2026, chap. 4, "People and software systems" section].

#### Containers

Applications and data stores that are needed in order to have a working system. Every container should have the following informations: Name, technology and description [@brown2026, chap. 4, "Containers" section].

#### Software system boundaries

The diagram should contain a box around containers to distinguish what is inside of the system [@brown2026, chap. 4, "Software system boundary" section].

#### Relationships

The diagram should contain unidirectional arrows between containers, people and outside software systems. Each arrow should be labeled with a description and where applicable the technology [@brown2026, chap. 4, "Relationships" section].

### Example

```mermaid
C4Container
    Person(athlete, "Athlete", "Records workouts and views statistics")

    System_Boundary(app, "Sports App") {
        Container(mobile, "Mobile App", "Kotlin", "Lets athletes record workouts and view statistics")
        Container(api, "API Application", "Spring Boot", "Provides workout and statistics functionality")
        ContainerDb(db, "Database", "PostgreSQL", "Stores workouts and user data")
    }

    System_Ext(tracker, "Fitness Tracker Platform", "Provides activity data recorded by wearables")

    Rel(athlete, mobile, "Records workouts and views statistics using")
    Rel(mobile, api, "Sends workouts to", "JSON/HTTPS")
    Rel(api, db, "Reads from and writes to", "SQL")
    Rel(api, tracker, "Imports activity data from", "JSON/HTTPS")

    UpdateRelStyle(athlete, mobile, $offsetX="-150", $offsetY="-40")
    UpdateRelStyle(mobile, api, $offsetX="-40", $offsetY="-50")

    UpdateLayoutConfig($c4ShapeInRow="2", $c4BoundaryInRow="1")
```
