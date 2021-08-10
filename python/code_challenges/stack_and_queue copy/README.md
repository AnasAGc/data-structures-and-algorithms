# Stacks and Queues
### Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

### A Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO).

## Challenge
+ Create a class called Stack, a class called Queue, and a class called Node

+ Node class has properties for the value stored in the Node, and a pointer to the next node.

+ Stack class has a top property. It creates an empty Stack when instantiated.

+ Queue class has a front property. It creates an empty Queue when instantiated

## Approach & Efficiency

First, i created a class called Node, that takes in a value, and define a value and a next property for every instance created, then i defined the Stack class, that has four methods for now, push is for appending a new node to the stack, pop is for removing a node form the stack, peek is to see whats the last value added to the stack, and isEmpty is to check if the stack is empty or not, exceptions were created in case of an empty stack.

then, i created a class called Queue, that has four methods, enqueue, that takes a value as an argument, then add the new node to the Queue, dequeue is to remove the first node out of the Queue, peek is to check the first node inside the Queue, and the isEmpty is to check if the queue is empty or not, exceptions were created in case of empty stack.
