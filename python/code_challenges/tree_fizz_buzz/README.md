
# Fizz Buzz Tree

Write a function called fizz buzz tree, that takes k-ary tree as an argument, and returns a copy of the k-ary tree with these changes:

replace the value by Fizz if the value is divisible by 3
replace the value by Buzz if the value is divisible by 5
replace the value by FizzBuzz if the value is divisible by 3 and 5

## WhiteBoard 
![The San Juan Mountains are beautiful!](https://i.ibb.co/QPbgCRX/Fizzbuzz.jpg "San Juan Mountains")

## Approach & Efficiency

i took the approach of storing all the nodes inside an array, and loop over them, then change the values to Fizz, Buzz, or FizzBuzz, the Big O is as follows:

for the time complexity => O(n), we have a while loop that loops over all the nodes in the solution

for the space complexity => O(1),  I just copy the value of the Tree without use any additional space. 

# Solution


```
  def fizz_buzz_tree(k_array):
   try:
     
        copy_root=copy.deepcopy(k_array)
        temp=Queue()
        temp.enqueue(copy_root.root)
        print(temp.front.value)

        while temp.front:

            [temp.enqueue(i) for i in temp.front.children if temp.front.children]

            if (temp.front.value % 3 == 0 and temp.front.value % 5 == 0):
                temp.front.value='FizzBuzz'

            elif temp.front.value % 3 == 0:
                temp.front.value='Fizz'

            elif temp.front.value % 5 == 0:
                temp.front.value='Buzz'   
                
            temp.dequeue()
            
        return copy_root
        
   except:
        raise ValueError('Empty Root')


```