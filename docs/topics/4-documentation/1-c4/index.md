# C4

The C4 model consists of:

- Four hierarchical abstractions: software systems, containers, components and code (Brown, 2026, Chapter 2)
- Four hierarchical diagrams: system context, containers, components and code (Brown, 2026, Chapter 2)
- Three supporting diagrams: system landscape, dynamic and deployment (Brown, 2026, Chapter 2, "Supporting Diagrams" section)

C4 is notation agnostic (Brown, 2026, Chapter 2, "Notation" section) and tool agnostic (Brown, n.d.).

## Abstractions

### Software systems

A software system is something that delivers value to its users and is mostly developed by one team (Brown, 2026, Chapter 2, "Software System" section).

### Containers

A container is a runnable unit. It is either an application or a data store (Brown, 2026, Chapter 2, "Container" section).

### Components

A component groups related functionality inside a container with well-defined interfaces (Brown, 2026, Chapter 2, "Component" section).

### Code

Code consists of the building blocks of the programming language like classes, interfaces or functions (Brown, 2026, Chapter 2, "Code" section).

---

## System Context Diagram

A system context diagram shows a software system with people and software systems interacting with it in a high-level view (Brown, 2026, Chapter 3).

### What

A single software system with people and software systems that interact with it (Brown, 2026, Chapter 3)

### Audience

Technical and non technical people, everybody involved in the project (Brown, 2026, Chapter 3)

### Content

Software systems, people and relationships (Brown, 2026, Chapter 3, "Content" section)

#### People

People who are using the system (prefered from a functional perspective) labeled with a name and a description (Brown, 2026, Chapter 3, "People" section).

#### Software systems

The software system that is described and the software systems that interact with it. Every software system, should be labeled with a name and a description (Brown, 2026, Chapter 3, "Software systems" section).

#### Relationships

Relationships should be created as "unidirectional arrows, each labeled with a summary of the relationship" (Brown, 2026, Chapter 3, "Relationships" section).

### Example

``` mermaid
C4Context
    Person(athlete, "Athlete", "Records workouts and views statistics")
    System(app, "Sports App", "Lets athletes track their workouts")
    System_Ext(tracker, "Fitness Tracker Platform", "Provides activity data recorded by wearables")

    Rel(athlete, app, "Records workouts and views statistics using")
    Rel(app, tracker, "Imports activity data from")

    UpdateLayoutConfig($c4ShapeInRow="1")
```

## Container Diagram

A container diagram shows the containers of a single software system (Brown, 2026, Chapter 4).

### What

Containers of a single software system (Brown, 2026, Chapter 4).

### Audience

Software architects and engineers (Brown, 2026, Chapter 4, "Audience" section)

### Content

#### People

People who are using a container of the software system (prefered from a functional perspective) labeled with a name and a description (Brown, 2026, Chapter 4, "People and software systems" section).

#### Software Systems

The software systems that interact with a container of the software system (Brown, 2026, Chapter 4, "People and software systems" section).

#### Containers

Applications and data stores that are needed in order to have a working system. Every container should have the following informations: Name, technology and description (Brown, 2026, Chapter 4, "Containers" section).

#### Software system boundaries

The diagram should contain a box around containers to distinguish what is inside of the system (Brown, 2026, Chapter 4, "Software system boundary" section).

#### Relationships

The diagram should contain unidirectional arrows between containers, people and outside software systems. Each arrow should be labeled with a description and where applicable the technology (Brown, 2026, Chapter 4, "Relationships" section).

### Example

``` mermaid
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

---

## Sources

Brown, S. (n.d.). *The C4 model*. C4 model. Retrieved October 24, 2026, from <https://web.archive.org/web/20261024081343/https://c4model.com/>

Brown, S. (2026). *The C4 model: Visualizing software architecture*. O’Reilly Media.

