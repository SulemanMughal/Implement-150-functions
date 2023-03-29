import random
    
    
random.seed(20)
    
    
def generate_random_point():
    return random.uniform(-1, 1), random.uniform(-1, 1)
    
    
def is_in_unit_circle(point):
    return point[0] ** 2 + point[1] ** 2 <= 1
    
    
points = [generate_random_point() for _ in range(15)]
flags = [is_in_unit_circle(point) for point in points]
print(flags)