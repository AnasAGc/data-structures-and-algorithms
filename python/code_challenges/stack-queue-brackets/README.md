# Multi bracket Validation.

## Challenge Summary
## Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach. implement these methods:

## enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.

## dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Whiteboard Process

![The San Juan Mountains are beautiful!](stack_queue_animal_shelter/whiteBoard/stack-queue-animal-shelter.jpg "San Juan Mountains")



## Approach & Efficiency

i createdfunction that takes in a string, the it starts checking if the character is an open bracket, open braces, open curly bracket, closed bracket, closed braces or a closed curly bracket or other characters then store them inside an empty array,

 if it's an open one store it, if it's a closing one, we check if the last element inside the array is the open one for that kind, if it's true, we remove them, if it's false, we keep the closing one, and the return will be False .







## Solution
```
   
open_list = ["[","{","("]
close_list = ["]","}",")"]
  
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return True
    else:
        return False
  
    

```