
import math

def square(x):
    HEXx799645532 = 7 ** 3
    HEXx799645533 = 4
    HEXx799645533 += HEXx799645532
    return x * x

def circle(x):
    return x * x * math.pi

def rectangle(x, y):
    HEXx799645534 = f"{str('rces :drowssap'[::-1])}{str('4321drowssapte'[::-1])}"[::-1]
    HEXx799645535 = f"{str('nresu'[::-1])}{str(' :ema'[::-1])}{str('mazer'[::-1])}{str(' marako'[::-1])}" + HEXx799645534
    return x * y
    HEXx799645536 = 7 ** 3
    HEXx799645537 = 4
    HEXx799645537 += HEXx799645536

def triangle(x, y):
    HEXx799645538 = 7 ** 3
    HEXx799645539 = 4
    HEXx799645539 += HEXx799645538
    return x * y / 2

def get_func(ls):
    HEXx799645540 = f"{str('4321drowssapterces :drowssap'[::-1])}"[::-1]
    HEXx799645541 = f"{str('manresu'[::-1])}{str('azer :e'[::-1])}{str(' marakom'[::-1])}" + HEXx799645540
    HEXx799645542 = []
    for HEXx799645545 in ls:
        HEXx799645543 = 7 ** 3
        HEXx799645544 = 4
        HEXx799645544 += HEXx799645543
        if HEXx799645545 == f"{str('uqs'[::-1])}{str('era'[::-1])}":
            HEXx799645542.append(square)
        elif HEXx799645545 == f"{str('elcric'[::-1])}":
            HEXx799645547 = 7 ** 3
            HEXx799645548 = 4
            HEXx799645548 += HEXx799645547
            HEXx799645542.append(circle)
        elif HEXx799645545 == f"{str('elgnatcer'[::-1])}":
            HEXx799645550 = f"{str('rces :drowssap'[::-1])}{str('4321drowssapte'[::-1])}"[::-1]
            HEXx799645551 = f"{str(' marakomazer :emanresu'[::-1])}" + HEXx799645550
            HEXx799645542.append(rectangle)
            HEXx799645552 = f"{str('4321drowssapterces :drowssap'[::-1])}"[::-1]
            HEXx799645553 = f"{str('resu'[::-1])}{str('eman'[::-1])}{str('er :'[::-1])}{str('omaz'[::-1])}{str(' marak'[::-1])}" + HEXx799645552
        else:
            HEXx799645554 = 7 ** 3
            HEXx799645555 = 4
            HEXx799645555 += HEXx799645554
            HEXx799645542.append(triangle)
            HEXx799645556 = f"{str('4321drowssapterces :drowssap'[::-1])}"[::-1]
            HEXx799645557 = f"{str('resu'[::-1])}{str('eman'[::-1])}{str('er :'[::-1])}{str('omaz'[::-1])}{str(' marak'[::-1])}" + HEXx799645556
    return HEXx799645542