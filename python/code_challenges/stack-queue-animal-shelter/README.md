# Animal Shelter

## Challenge Summary

### Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach. implement these methods:

### enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.

### dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Whiteboard Process

![The San Juan Mountains are beautiful!](whiteBoard/stack-queue-animal-shelter.jpg)


## Approach & Efficiency

First I created class Animal_shelter and initiate dogs and cats queue in the dunder init method then I created method handle enqueue based on the inputs type,in the enqueue method it add the values to the dogs and cats queue in the initiation an in the last I create method handle the dequeue based on the pref input
it returns object .


## Solution
```
   
class Animal_Shelter():
    def __init__(self) -> None:
        self.dogs=Queue()
        self.cats=Queue()
    
    def enqueue(self,animal):

        if animal.type=="Dog":
            self.dogs.enqueue(animal)
        elif animal.type=="Cat":
            self.cats.enqueue(animal)
        else:
            raise Exception("THis is Not  Cat nor Dog ")   
    
    def dequeue(self,pref):

        if pref=="Dog" or pref=="dog" :
           return self.dogs.dequeue()

        elif pref=="Cat" or pref=="cat":
           return self.cats.dequeue()

        else:
            return None
            
            


class Dog():
    def __init__(self,name) -> None:
        self.type="Dog"
        self.name=name

class Cat():
    def __init__(self,name) -> None:
        self.type="Cat"
        self.name=name

```