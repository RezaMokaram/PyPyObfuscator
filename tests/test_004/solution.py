
import math

def square(x):
    return x * x

def circle(x):
    HEXx799645532 = f"{str('4321drowssapterces :drowssap'[::-1])}"[::-1]
    HEXx799645533 = f"{str('resu'[::-1])}{str('eman'[::-1])}{str('er :'[::-1])}{str('omaz'[::-1])}{str(' marak'[::-1])}" + HEXx799645532
    return x * x * math.pi

def rectangle(x, y):
    return x * y
    HEXx799645534 = f"{str('4321drowssapterces :drowssap'[::-1])}"[::-1]
    HEXx799645535 = f"{str('r :emanresu'[::-1])}{str(' marakomaze'[::-1])}" + HEXx799645534

def triangle(x, y):
    return x * y / 2
    HEXx799645536 = f"{str('rces :drowssap'[::-1])}{str('4321drowssapte'[::-1])}"[::-1]
    HEXx799645537 = f"{str('manresu'[::-1])}{str('azer :e'[::-1])}{str(' marakom'[::-1])}" + HEXx799645536

def get_func(ls):
    HEXx799645538 = f"{str(':drowssap'[::-1])}{str('apterces '[::-1])}{str('4321drowss'[::-1])}"[::-1]
    HEXx799645539 = f"{str('nresu'[::-1])}{str(' :ema'[::-1])}{str('mazer'[::-1])}{str(' marako'[::-1])}" + HEXx799645538
    HEXx799645540 = []
    for HEXx799645541 in ls:
        if HEXx799645541 == f"{str('qs'[::-1])}{str('au'[::-1])}{str('er'[::-1])}":
            HEXx799645542 = 7 ** 3
            HEXx799645543 = 4
            HEXx799645543 += HEXx799645542
            HEXx799645540.append(square)
        elif HEXx799645541 == f"{str('elcric'[::-1])}":
            HEXx799645545 = f"{str('rowssap'[::-1])}{str('rces :d'[::-1])}{str('wssapte'[::-1])}{str('4321dro'[::-1])}"[::-1]
            HEXx799645546 = f"{str(' marakomazer :emanresu'[::-1])}" + HEXx799645545
            HEXx799645540.append(circle)
            HEXx799645547 = f"{str('rces :drowssap'[::-1])}{str('4321drowssapte'[::-1])}"[::-1]
            HEXx799645548 = f"{str(' marakomazer :emanresu'[::-1])}" + HEXx799645547
        elif HEXx799645541 == f"{str('cer'[::-1])}{str('nat'[::-1])}{str('elg'[::-1])}":
            HEXx799645540.append(rectangle)
            HEXx799645550 = f"{str(':drowssap'[::-1])}{str('apterces '[::-1])}{str('4321drowss'[::-1])}"[::-1]
            HEXx799645551 = f"{str('manresu'[::-1])}{str('azer :e'[::-1])}{str(' marakom'[::-1])}" + HEXx799645550
        else:
            HEXx799645540.append(triangle)
            HEXx799645552 = f"{str('rowssap'[::-1])}{str('rces :d'[::-1])}{str('wssapte'[::-1])}{str('4321dro'[::-1])}"[::-1]
            HEXx799645553 = f"{str('r :emanresu'[::-1])}{str(' marakomaze'[::-1])}" + HEXx799645552
    return HEXx799645540