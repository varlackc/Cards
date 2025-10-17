# Documentation for the Cards program

This are the instructions on how to use the card program.

Each card contains both `rank` and `suite`.
Eeach card is represented as a `tuple` of both `suite` and `rank`.

Additional elements that are part of the car program include `card decks` and `card hands`.

## How to call the Cards project files

The first step is to import the files in the `card` folder and select the classes that contain the components that you are trying to use. The following example shows how to call the `card` class:

```python
from card import Card
```

There is also the possibility of importing all of the classes in the project using the following call:

```python
from card import *
```

We then will have to call the instance of the `card` before we could take any action with the `card`. The same is true for the `deck`, `hand` or `discard`. The process will look as follows:

```
c1 = Card()
```

The value of the card will have to be set after the card is created. We can set the card value by using the set_card method. In such case we will set the suite and rank of the card as inputs. we can do it as shown in the
following example:

```
c1.set_card("Heart","A")
```

We can verify the content of the card by using the get_card method. It will return the suite and rank of the card inside a tuple. 

```
c1.get_card()
```