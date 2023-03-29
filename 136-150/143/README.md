# Exercise No. 143


The *Stack* class has been implemented.

Implement a function called `transfer()` that moves all the elements of the first stack to the second stack, so that the item at the top of the first stack is the first item to be inserted into the second stack.

The `transfer()` function takes two arguments:

-   stack_1 - the first stack to transfer items from

-   stack_2 - second stack to transfer items to

and return the given stacks.


**Example:**


    s1 = Stack()
    s1.push('python')
    s1.push('java')
    s1.push('c++')
     
    s2 = Stack()
    s2.push('sql')
     
    s1, s2 = transfer(s1, s2)


    [IN]: len(s1), len(s2)
    [OUT]: (0, 4)
     
    [IN]: s2.pop()
    [OUT]: 'python'
     
    [IN]: s2.pop()
    [OUT]: 'java'


You just need to implement the `transfer()` function. The tests run several test cases to validate the solution.