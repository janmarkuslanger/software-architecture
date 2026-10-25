# System Landscape Diagram

## What
A system landscape diagram shows how multiple software systems work together. This is one level above the system context diagram[@brown2026, chap. 9].

## Audience 
Technical and non technical people, everybody involved in the project [@brown2026, chap. 9, "Audience" section]

## Content 

The diagram should show the software systems and people who use it [@brown2026, chap. 9, "Content" section].  

## Example

```mermaid
C4Context
    Person(athlete, "Athlete", "Records workouts and views statistics")
    Person(support, "Support Agent", "Helps athletes with their accounts")

    Enterprise_Boundary(company, "Sports Company") {
        System(app, "Sports App", "Lets athletes track their workouts")
        System(supportSystem, "Support System", "Manages support tickets")
        System(subscription, "Subscription System", "Manages premium subscriptions")
        System(email, "E-Mail System", "Sends notifications to athletes")
    }

    Boundary(external, "External") {
        System_Ext(payment, "Payment Provider", "Processes card payments")
        System_Ext(tracker, "Fitness Tracker Platform", "Provides activity data recorded by wearables")
    }

    Rel(athlete, app, "Records workouts and views statistics using")
    Rel(support, supportSystem, "Handles tickets using")
    Rel(supportSystem, app, "Looks up accounts in")
    Rel(app, subscription, "Checks premium status using")
    Rel(subscription, email, "Sends invoices using")
    Rel(subscription, payment, "Charges subscriptions using")
    Rel(app, tracker, "Imports activity data from")

    UpdateRelStyle(athlete, app, $offsetX="-60", $offsetY="-30")
    UpdateRelStyle(supportSystem, app, $offsetX="-45", $offsetY="-35")
    UpdateRelStyle(subscription, email, $offsetX="-45", $offsetY="-35")

    UpdateLayoutConfig($c4ShapeInRow="2", $c4BoundaryInRow="1")
```
