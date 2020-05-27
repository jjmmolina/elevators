# elevators
Elevators exercise for Sewan recruitment process.
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
- **File _elevators.py_** -> It includes the class **Elevators**, that represents an elevator.
- **File _floors.py_** -> It includes the class **Floors**, that represents a floor.
- **File _requests_elevators.py_** -> It includes the class **Requests_Elevators**, that represents a request.

## Functionalities implemented

## Usage


## Tests
All tests are implemented in the folder called test. This includes:
- Tests for elevator movement.
- Tests for requests.

You can launch the test suite by running the following command:

    python -m unittest
 
 ## TO-DO list