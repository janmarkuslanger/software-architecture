# Code Diagram

## What
A code diagram shows the internal code structure of a component [@brown2026, chap. 6].


## Audience 
Engineers [@brown2026, chap. 6, "Audience" section]

## Content 

The code diagram should "show the various code-level building blocks supported by the programming language being used" [@brown2026, chap. 6, "Content" section].

## Example

```mermaid
classDiagram
    direction LR

    class WorkoutService {
        +recordWorkout(workout: Workout) Workout
        +getStatistics(athleteId: UUID) WorkoutStatistics
        +importActivities(athleteId: UUID) void
    }

    class WorkoutStatistics {
        +totalWorkouts: int
        +totalDistanceKm: double
        +totalDuration: Duration
    }

    class Workout {
        +id: UUID
        +athleteId: UUID
        +type: WorkoutType
        +startedAt: Instant
        +duration: Duration
        +distanceKm: double
    }

    class WorkoutRepository {
        <<interface>>
        +save(workout: Workout) Workout
        +findByAthleteId(athleteId: UUID) List~Workout~
    }

    class TrackerClient {
        <<interface>>
        +fetchActivities(athleteId: UUID) List~Workout~
    }

    WorkoutService --> WorkoutRepository : uses
    WorkoutService --> TrackerClient : uses
    WorkoutService ..> WorkoutStatistics : creates
    WorkoutService ..> Workout : handles
```
