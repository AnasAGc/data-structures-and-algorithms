
# Breadth First

Write a function called fizz buzz tree, that takes k-ary tree as an argument, and returns a copy of the k-ary tree with these changes:

replace the value by Fizz if the value is divisible by 3
replace the value by Buzz if the value is divisible by 5
replace the value by FizzBuzz if the value is divisible by 3 and 5

## WhiteBoard 
![The San Juan Mountains are beautiful!](https://i.ibb.co/2nFsSNZ/breadthfirst.jpg "San Juan Mountains")

## Approach & Efficiency

i took the approach of storing all the nodes inside an array, and loop over them, then change the values to Fizz, Buzz, or FizzBuzz, the Big O is as follows:

for the time complexity => O(n), we have a while loop that loops over all the nodes in the solution

for the space complexity => O(n), we have a list that is directly dependent on a while loop to store the values

# Solution


```
  def breadthFirst():

        if not root:
                raise Exception("Empty Tree")

        Queue_breadth = Queue()
        Queue_breadth.enqueue(root)

        try:
            while Queue_breadth.peek():
                
                    node_front = Queue_breadth.dequeue()
                    
                    self.arr.append(node_front.value)

                    if node_front.left:
                        Queue_breadth.enqueue(node_front.left)

                    if node_front.right:
                        Queue_breadth.enqueue(node_front.right)
            
        except:
            return self.arr

```