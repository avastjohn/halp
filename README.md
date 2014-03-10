# HALP

## Goals For This App

* Students can make a help request, or second another student's help request, and mark the request as urgent or non-urgent
* Teachers can see all current help requests on their phone/tablet in chronological order and decide who to help first or when to pause the activity to regroup and clarify common misunderstandings
* Students can cancel their help requests if they figure it out on their own
* Students can elect to help other students if they recognize the problem and have the solution

## Tech Stack

* Python/Flask/SQLAlchemy back end
* JS/jQuery/HTML/CSS front end
* Plan to deploy to Heroku

### Status

* Adding a help request or hitting nevermind button updates the db
* Next steps: 
* * make non-urgent requests yellow
* * keep track of number of request hits on one topic/display that number/delete request only if all requesters hit nevermind button
* * make requests responsive