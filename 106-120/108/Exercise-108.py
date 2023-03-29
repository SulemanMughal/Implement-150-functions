from itertools import cycle
    
    
def spiral_matrix(size):
    # Preparing an empty matrix
    matrix = [[None] * size for _ in range(size)]
    
    # Starting point
    x, y = 0, 0
    
    # (0, 1) represents moving right along the matrix row
    # (0, -1) represents moving left along the matrix row
    # (1, 0) represents moving down along the matrix column
    # (-1, 0) represents moving up along the matrix column
    movements = cycle(((0, 1), (1, 0), (0, -1), (-1, 0)))
    dx, dy = next(movements)
    
    for i in range(size**2):
        matrix[x][y] = i + 1
        xdx = x + dx
        ydy = y + dy
        if (
            not 0 <= xdx < size
            or not 0 <= ydy < size
            or matrix[xdx][ydy] is not None
        ):
            dx, dy = next(movements)
        x += dx
        y += dy
    return matrix