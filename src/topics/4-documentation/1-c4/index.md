# C4

The C4 model consists of:

- Four hierarchical abstractions: software systems, containers, components and code [@brown2026]
- Four hierarchical diagrams: system context, containers, components and code [@brown2026]
- Three supporting diagrams: system landscape, dynamic and deployment [@brown2026]

C4 is notation and tool agnostic [@brown2026].

## Abstractions

### Software systems

A software system is something that delivers value to its users and is mostly developed by one team [@brown2026].

### Containers

A container is a runnable unit. It is either an application or a data store [@brown2026].

### Components

A component groups related functionality inside a container with well-defined interfaces [@brown2026].

### Code

Code consists of the building blocks of the programming language like classes, interfaces or functions [@brown2026].

## Diagrams

### System Context Diagram

A system context diagram shows a software system in its nearest context in a high level view. 

### What
A system context and its context [@brown2026]

### Audience 
Technincal and non technical people, everybody involved in the project

### Content 

Software systems, people and relationships [@brown2026]

#### People

People who are using the system (prefered from a functional perspective) labeled with a name and a description. 


#### Software systems

The software system that is described and the software systems in its relationship. Every software syste, should be labeled with a name and a description.  

#### Relationships

Relationships should be created as "unidirectional arrows, each labeled with a summary of the relationship“. 



### Container Diagram

A system context diagram shows the containers of a single software system. 