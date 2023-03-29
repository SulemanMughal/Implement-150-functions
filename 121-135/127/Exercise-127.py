import random
    
    
random.seed(10)
    
    
def generate_random_point():
    return random.uniform(-1, 1), random.uniform(-1, 1)
    
    
def is_in_unit_circle(point):
    return point[0] ** 2 + point[1] ** 2 <= 1
    
    
def estimate(simulations):
    points_in_circle = 0
    for _ in range(simulations):
        point = generate_random_point()
        if is_in_unit_circle(point):
            points_in_circle += 1
    result = 4 * points_in_circle / simulations
    return result