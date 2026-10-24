# C4

The C4 model consists of:

- Four hierarchical abstractions: software systems, containers, components and code (Brown, 2026)
- Four hierarchical diagrams: system context, containers, components and code (Brown, 2026)
- Three supporting diagrams: system landscape, dynamic and deployment (Brown, 2026)

C4 is notation and tool agnostic (Brown, 2026).

## Abstractions

### Software systems

A software system is something that delivers value to its users and is mostly developed by one team (Brown, 2026).

### Containers

A container is a runnable unit. It is either an application or a data store (Brown, 2026).

### Components

A component groups related functionality inside a container with well-defined interfaces (Brown, 2026).

### Code

Code consists of the building blocks of the programming language like classes, interfaces or functions (Brown, 2026).

---

## System Context Diagram

A system context diagram shows a software system in its nearest context in a high level view.

### What

A system context and its context (Brown, 2026)

### Audience

Technical and non technical people, everybody involved in the project

### Content

Software systems, people and relationships (Brown, 2026)

#### People

People who are using the system (prefered from a functional perspective) labeled with a name and a description.

#### Software systems

The software system that is described and the software systems in its relationship. Every software syste, should be labeled with a name and a description.

#### Relationships

Relationships should be created as "unidirectional arrows, each labeled with a summary of the relationship“.

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

A system context diagram shows the containers of a single software system.

### What

Containers of a single software system.

### Audience

Software architects and engineers

### Content

#### People

People who are using the system (prefered from a functional perspective) labeled with a name and a description.

#### Software Systems

The software systems that interact with the described single software system.

#### Containers

Applications and data stores that are needed in order to have a working system. Every container should have the following informations: Name, technology and description.

#### Software system boundaries

The diagram should contain a box around containers to distinguish what is inside of the system.

#### Relationships

The diagram should contain unidirectional arrows between containers. Each arrow should be labeled with a name and the technology.

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

Brown, S. (2026). *The C4 model: Visualizing software architecture*. O’Reilly Media.

