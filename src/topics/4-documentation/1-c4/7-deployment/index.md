# Deployment Diagram

## What

A deployment diagram is a "way to diagram the deployment topology" [@brown2026, chap. 8] for a software system. 

## Audience

Software architects and engineers [@brown2026, chap. 8, "Audience" section].

## Content

### Container instances

The container instances inside the software system [@brown2026, chap. 8, "Container instances" section].

### Software system instances

Software system instances running outside of the current scope of the software system that interact with the current software system [@brown2026, chap. 8, "Software system diagram" section]. 

### Deployment nodes

A building block of infrastructure where a container is running [@brown2026, chap. 8, "Deployment nodes" section]. 

### Infrastructure nodes

An infrastructure node is a building block of infrastructure such as a load balancer or gateway [@brown2026, chap. 8, "Infrastructure nodes" section]. 

## Example

```mermaid
C4Deployment
    title Sports App - Production

    Deployment_Node(phone, "Athlete's smartphone", "Android") {
        Container(mobile, "Mobile App", "Kotlin", "Lets athletes record workouts and view statistics")
    }

    Deployment_Node(aws, "Amazon Web Services", "eu-central-1") {
        Container(lb, "Load Balancer", "AWS Application Load Balancer", "Infrastructure node that distributes requests")

        Deployment_Node(ecs, "ECS Cluster", "AWS Fargate") {
            Container(api, "API Application", "Spring Boot", "Provides workout and statistics functionality")
        }

        Deployment_Node(rds, "Amazon RDS", "Managed PostgreSQL") {
            ContainerDb(db, "Database", "PostgreSQL", "Stores workouts and user data")
        }
    }

    System_Ext(tracker, "Fitness Tracker Platform", "Provides activity data recorded by wearables")

    Rel(mobile, lb, "Sends workouts to", "JSON/HTTPS")
    Rel(lb, api, "Forwards requests to", "JSON/HTTPS")
    Rel(api, db, "Reads from and writes to", "SQL")
    Rel(api, tracker, "Imports activity data from", "JSON/HTTPS")

    UpdateRelStyle(mobile, lb, $offsetX="-50", $offsetY="-35")
    UpdateRelStyle(lb, api, $offsetX="10", $offsetY="-60")
    UpdateRelStyle(api, tracker, $offsetX="-180", $offsetY="-235")
    UpdateRelStyle(api, db, $offsetX="-60", $offsetY="-30")

    UpdateElementStyle(lb, $bgColor="#ffffff", $fontColor="#333333", $borderColor="#888888")

    UpdateLayoutConfig($c4ShapeInRow="2", $c4BoundaryInRow="2")
```
