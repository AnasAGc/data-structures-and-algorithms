# Challenge Summary
Write a function called business trip, that takes a graph and an array of city names as an input, calculates the total cost and return the total cost if the trip can be done, or a none if it's not possible

## Whiteboard Process

![image](https://i.ibb.co/R06SKCH/linked-list-insertions-append-18.jpg)

## Approach & Efficiency

the approach used assures that there is no edge case that can happen at all
+  Define  a function called business_trip takes to parameter graph and list of city.
+  define cost and i and length to store the len of the array.
+  define Breadth as Queue
+  define helper function that take two arguments
+  declare neighbors variable and assign to it the value from graph.get neighbors method with first parameter.
+  loop  when city is exist in the neighbors and :
 check if the value of the first node equal node if yes : add the cost to the cost and increment i by one
+  check if i equal the length of list then return else
 invoke the helper function again
+  in the main function call the helper function and make
+ return cost and bool (true or false)

## Solution

```


def business_trip(graph,arr):
    """
    Determine whether the trip is possible with direct flights, and how much it would cost.



    Args:
        graph (Graph): contains all the list of the cities and its cost
        arr (list): List of the cities
    Return
        tuple : (cost, Bool).
            
            cost: Total cost for Trip.
            Bool: True or False.
     

    """
    
    cost=0
    i=0
    length=len(arr)-1

    def check_cost(city1,city2):
     ''' Calculate the Cost value for the Trip between two City  '''
     neighbors=graph.get_neighbors(city1)
     for city in neighbors:
            if city.vertex.value == city2:
             nonlocal cost , i
             cost += city.weight
             i+=1
             
            if i == length:
                return
     check_cost(arr[length-i-1],arr[length-i])
     

    try:
     check_cost(arr[length-1],arr[length])
    except:
     return (bool(cost),cost)
 
    return (bool(cost),cost)



```