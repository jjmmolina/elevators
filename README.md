# Elevators
Elevators exercise for my current company recruitment process. 

## Specifications
The purpose of this exercise is to model an elevator cluster simulator in a building.
We’ll have in this building n floors served by x elevators.
Each elevator in the cluster must obey the following rules:

**General Properties**

- An elevator must serve all pending requests on his way, providing they are in its
current direction.
- The order of the requests is always the order of the floors according to the
current direction.
- The timing of the requests must be taken into account.
- If there’s no available elevator to answer a request, the request is cancelled.
- The default position for an elevator is the first floor. If an elevator is no more
requested, it must then return to the first floor.

**Outside calls**

- At each floor — except the first one and the last one, the request can be made in
two directions. At the first floor, it is only possible to call an elevator to go up and,
at the last floor, it’s only possible to call an elevator to go down.
- When a request is made from a floor, only the nearest elevator going in the
direction of the request can answer. If no elevator is currently in use, a default
elevator will answer the request.
- An elevator cannot answer more than n/x request. If such case arises, another
elevator will take over.

**Inside calls**

- It is not possible to choose a floor that goes in the opposite direction of the
outside call.

## Prev requirements

To install the dependencies execute the following command in a virtual python environment:

    pip install -r requirements

## Classes
The code is divided in classes (inside folder _models_). 
- **File _building.py_** -> It includes the class **Building**, that represents a building with floors and elevators.
This is the dispatcher element of the application. See Branches section for more explications.
- **File _elevators.py_** -> It includes the class **Elevators**, that represents an elevator.
- **File _requests_elevators.py_** -> It includes the class **Requests_Elevators**, that represents a request.

## Branches
This exercise contains two branches: Master and Dev. **_Master_** is the principal branch and this is a sequential version to 
resolve the problem: in this case, Building class is a dispatcher that assign each request to the best elevator according
to the requirements. Elevator only should to go to the floor, to collect the passengers in each floor in which it should to
stop, and to arrive to the destination floor. **_Dev_** branch is a improvement of the problem resolution. It contains the
same classes but the orientation is different. In this cases, Building class only launches all building elevators, each 
of them in a thread. Then, each elevator contains a run method that look for the best request that could be dispatch, 
and do it. **This second version is not finished** (for this is in this branch, and not in the Master branch).

## Usage
You can run the application executing the following command

```
python play.py -f 5 -e 2 -r 7
```
Where 
- '--floors' or  '-f' is the number of floors in the building
- '--elevators' or  '-e' is the number of elevators working ind the building
- '--requests'or '-r' is the number of simulated requests to run the application

With this data, application runs a scenario with this values
 
## Tests
I have followed a TDD strategy to resolve the problem. All tests are implemented in the folder called test. 
This includes test to check movements, calls, to validate floors, to validate directions, etc. Of course 
(**and I said during my video-interview**), all test could be better. In my 
current job is very difficult to develop with a TDD strategy, and it is a great mistake. What I want to say with this 
is that probably all test are available to improve.

You can launch the test suite by running the following command:

    python -m unittest
 
 ## TO-DO list
 - Improve command line, allowing introduce requests manually
 - Finish thread version
 - User interface
