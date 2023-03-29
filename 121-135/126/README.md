# Exercise No. 126

**Monte Carlo methods** are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. The underlying concept is to use randomness to solve problems that might be deterministic in principle. They are often used in physical and mathematical problems and are most useful when it is difficult or impossible to use other approaches.

Let's use the Monte Carlo method to approximate Pi. Consider the coordinate system in R^2 space and a circle with a radius of 1 centered at (0, 0). The area of the circle is equal to Pi. Let's add a square on this circle with vertices at (1, 1), (1, -1), (-1, -1), (-1, 1). The side of this square is equal to 2 and its area is equal to 4.

Our task is to draw points from the given square according to the uniform distribution and check whether the drawn point falls into the circle. The probability of such an event is equal to the area of the circle with radius 1, which is exactly Pi.

We choose the number of simulations freely, but basically the more simulations we run, the better the approximation of Pi will be obtained.


The area of a circle can be calculated from the formula:


    area of the circle = area of the square * (number of points drawn inside the circle / number of all points drawn)


Since we know that the area of the circle is equal to Pi, we can substitute:


    Pi = area of the square * (number of points drawn inside the circle / number of all points drawn)


A function called `generate_random_point()` has been implemented, which generates a point with coordinates between [-1, 1] according to the uniform distribution.


Implement a function called `is_in_unit_circle()` that checks if a given point falls into a circle with a radius of 1. The function returns True if the point is inside the circle, otherwise False.


Set a random seed to 20 and pseudo-randomly generate 15 points by assigning them to a list called points. Then call the `is_in_unit_circle()` function at each point in the list and assign it to the variable flags. In response, print the contents of the flags variable to the console.


**Expected result:**


    [True, True, True, False, True, False, True, True, True, True, True, True, True, False, True]


