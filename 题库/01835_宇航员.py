for _ in range(int(input())):
    n = int(input())
    position = [0, 0, 0]
    front = [1, 0, 0]
    above = [0, 0, 1]


    def reverse(x):
        return [-i for i in x]


    def cross(x, y):
        z = [0, 0, 0]
        z[0] = x[1] * y[2] - x[2] * y[1]
        z[1] = x[2] * y[0] - x[0] * y[2]
        z[2] = x[0] * y[1] - x[1] * y[0]
        return z


    for _ in range(n):
        turn, step = input().split()
        step = int(step)
        if turn == 'forward':
            pass
        if turn == 'back':
            front = reverse(front)
        if turn == 'left':
            front = cross(above, front)
        if turn == 'right':
            front = cross(front, above)
        if turn == 'up':
            front, above = above, reverse(front)
        if turn == 'down':
            front, above = reverse(above), front
        for i in range(3):
            position[i] += step * front[i]
    matrix = [[0, 0, 3], [0, 4, 1], [0, 2, 5]]
    p = sum([matrix[i][front[i]] for i in range(3)])
    print(f'{position[0]} {-position[1]} {position[2]} {p}')
