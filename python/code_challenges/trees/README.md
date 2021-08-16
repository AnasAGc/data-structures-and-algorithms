
# Breadth First

Write a function called breadth first that accept the root of the tree and return the values in array



## WhiteBoard 
![The San Juan Mountains are beautiful!](https://i.ibb.co/2nFsSNZ/breadthfirst.jpg "San Juan Mountains")

## Approach & Efficiency

I used the queue data struction to implement the breadthFirst order as it shown in the Solution  


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