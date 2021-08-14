
# Trees

Find the Maximum Value in a Binary Tree, create a method that takes no inputs, and returns the maximum value inside the Binary Tree

## Challenge

write funtion to  find maximum value taks Arguments: none and Returns: number

## WhiteBoard 
![The San Juan Mountains are beautiful!](https://i.ibb.co/9TVBndC/find-max.jpg "San Juan Mountains")

## Approach & Efficiency

I used the in_order to get the values of the Tree in list then I loop to find the max value in the array. 


# Solution

```
def tree_max(self):

        x=self.in_order(self.root)
        self.max=0

        for i in x :
            if i>self.max:
                self.max=i
        return self.max

```