import math

def square(x):
    return x * x

def circle(x):
    return x * x * math.pi

def rectangle(x, y):
    return x * y

def triangle(x, y):
    return (x * y) / 2

def get_func(ls):
    new_ls = []
    for i in ls:
        if i == 'square':
            new_ls.append(square)
        elif i == 'circle':
            new_ls.append(circle)
        elif i == 'rectangle':
            new_ls.append(rectangle)
        else:
            new_ls.append(triangle)
    return new_ls