# Dynamic Diagram

## What

A dynamic diagram shows software processes during runtime (Brown, 2026, Chapter 7).

## Audience

The audience depends on the abstraction level. The audience will be the same as the diagram abstraction level (Brown, 2026, Chapter 7, "Audience" section).

## Content

A dynamic diagram has no fixed set of elements. It can be drawn as a UML sequence diagram or a UML collaboration diagram (Brown, 2026, Chapter 7, "Content" section).

## Example

``` mermaid
C4Dynamic
    title Import of activity data

    System_Ext(tracker, "Fitness Tracker Platform", "Provides activity data recorded by wearables")

    System_Boundary(app, "Sports App") {
        Container(mobile, "Mobile App", "Kotlin", "Lets athletes record workouts and view statistics")
        ContainerDb(db, "Database", "PostgreSQL", "Stores workouts and user data")

        Container_Boundary(api, "API Application") {
            Component(workoutController, "Workout Controller", "Spring MVC REST Controller", "Provides endpoints for workouts and statistics")
            Component(trackerClient, "Tracker Client", "Spring Bean", "Fetches activity data from the fitness tracker platform")
            Component(workoutService, "Workout Service", "Spring Bean", "Handles workouts and calculates statistics")
            Component(workoutRepository, "Workout Repository", "Spring Data JPA", "Reads and writes workouts")
        }
    }

    RelIndex(1, mobile, workoutController, "Requests import of activities", "JSON/HTTPS")
    RelIndex(2, workoutController, workoutService, "Starts import")
    RelIndex(3, workoutService, trackerClient, "Requests activities")
    RelIndex(4, trackerClient, tracker, "Fetches activity data from", "JSON/HTTPS")
    RelIndex(5, workoutService, workoutRepository, "Saves workouts")
    RelIndex(6, workoutRepository, db, "Writes workouts to", "SQL")

    UpdateRelStyle(trackerClient, tracker, $offsetX="-200", $offsetY="-140")
    UpdateRelStyle(workoutRepository, db, $offsetX="0", $offsetY="-150")
    UpdateRelStyle(workoutService, workoutRepository, $offsetX="-30", $offsetY="-30")
    UpdateRelStyle(mobile, workoutController, $offsetX="-160", $offsetY="-30")

    UpdateLayoutConfig($c4ShapeInRow="2", $c4BoundaryInRow="1")
```

---

## Sources

Brown, S. (2026). *The C4 model: Visualizing software architecture*. O’Reilly Media.

