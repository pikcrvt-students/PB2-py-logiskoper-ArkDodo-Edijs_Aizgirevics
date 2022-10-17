"""
System to do 6 figure tasks and 3 logical operations.
Author: Edijs Aizgirevičs DP 2-1
"""

import doctest

def isInside_rec1(x, y):
    """
    >>> isInside_rec1(-1.5, 1)
    On edge.
    >>> isInside_rec1(0, 1.5)
    Inside.
    >>> isInside_rec1(-1, -1)
    On edge.
    >>> isInside_rec1(-3, 0.5)
    Inside
    >>> isInside_rec1(-6, 6)
    Outside.
    """
    if -1 <= x <= 3 or -2 <= y <= 1:
        if x == -1 or x == 3 or y == -2 or y == 1:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_rec2(x, y):
    """
    >>> isInside_rec2(-1.5, 1)
    On edge.
    >>> isInside_rec2(0, 3)
    On edge.
    >>> isInside_rec2(-1, 1)
    Inside.
    >>> isInside_rec2(-3, 2)
    Inside
    >>> isInside_rec2(-10, -10)
    Outside.
    """
    if -5 <= x <= 2 or -1 <= y <= 3:
        if x == -5 or x == 2 or y == 1 or y == 3:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_tri(x, y):
    """
    >>> isInside_tri(0, 1)
    On edge.
    >>> isInside_tri(1, 0)
    On edge.
    >>> isInside_tri(1, 2)
    Inside.
    >>> isInside_tri(1.5, 2)
    Inside
    >>> isInside_tri(-20, 20)
    Outside.
    """
    if 0 <= x <= 2 or 0 <= y <= -1.5 * x + 3:
        if x == 0 or y == 0 or y == -1.5 * x + 3:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_cir(x, y):
    """
    >>> isInside_cir(0.5, 1)
    On edge.
    >>> isInside_cir(1, 1)
    On edge.
    >>> isInside_cir(0.5, 0.7)
    Inside.
    >>> isInside_cir(25, -200)
    Outside
    >>> isInside_cir(-6, 6)
    Outside.
    """
    if (x ** 2 + y ** 2) ** 0.5 <= 1:
        if (x ** 2 + y ** 2) ** 0.5 == 1:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_cut_cir(x, y):
    """
    >>> isInside_cut_cir(-1, 2)
    On edge.
    >>> isInside_cut_cir(-2, 3)
    On edge.
    >>> isInside_cut_cir(-2, 2)
    Inside.
    >>> isInside_cut_cir(25, -200)
    Outside.
    >>> isInside_cut_cir(-100, -100)
    Outside.
    """
    if ((-2 - x) ** 2 + (2 - y) ** 2) ** 0.5 <= 1 and y <= x + 5:
        if ((-2 - x) ** 2 + (2 - y) ** 2) ** 0.5 == 1 or y == x + 5 and ((-2 - x) ** 2 + (2 - y) ** 2) ** 0.5 < 1:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_trap(x, y):
    """
    >>> isInside_trap(-3, -1)
    On edge.
    >>> isInside_trap(0, -2.5)
    On edge.
    >>> isInside_trap(-1, -1)
    Inside.
    >>> isInside_trap(-2.5, -2)
    Inside
    >>> isInside_trap(-20, 20)
    Outside.
    """
    if 0 <= x <= -3 or -2.5 >= y >= 2 / 3 * x + 2:
        if x == 0 or x == -3 or y == -2.5 or y == 2 / 3 * x + 2:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_point1(x):
    """
    >>> isInside_point1(5)
    Inside.
    >>> isInside_point1(456)
    Inside
    >>> isInside_point1(-2)
    Outside.
    >>> isInside_point1(3)
    Outside.
    """
    if x > 3:
        print("Inside.")
    else:
        print("Outside.")


def isInside_point2(x):
    """
    >>> isInside_point2(9)
    On edge.
    >>> isInside_point2(8)
    Inside.
    >>> isInside_point2(-6)
    Inside.
    >>> isInside_point2(-254)
    Inside
    >>> isInside_point2(15)
    Outside.
    """
    if x <= 9:
        if x == 9:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_point3(x):
    """
    >>> isInside_point3(-4)
    On edge.
    >>> isInside_point3(-3)
    Inside.
    >>> isInside_point3(1)
    Inside.
    >>> isInside_point3(0)
    Inside
    >>> isInside_point3(45)
    Outside.
    """
    if -4 <= x < 2:
        if x == -4:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


# Driver Code
print("Chose your task type.\n"
      "Type 1 is figure tasks.\n"
      "Type 2 is linear tasks.")
while True:
    tipe = int(input("Input type nr."))
    if tipe == 1 or tipe == 2:
        break

if tipe == 1:
    print("Task 1 is rectangle\n"
          "Task 2 is rectangle\n"
          "Task 3 is triangle\n"
          "Task 4 is circle\n"
          "Task 5 is cut circle\n"
          "Task 6 is trapeze")
    while True:
        task = int(input("Input task nr."))
        if task == 1 or task == 2 or task == 3 or task == 4 or task == 5 or task == 6:
            break
    x = float(input("Input x point coordinates: "))
    y = float(input("Input y point coordinates: "))
    if task == 1:
        isInside_rec1(x, y)
    if task == 2:
        isInside_rec2(x, y)
    if task == 3:
        isInside_tri(x, y)
    if task == 4:
        isInside_cir(x, y)
    if task == 5:
        isInside_cut_cir(x, y)
    if task == 6:
        isInside_trap(x, y)

if tipe == 2:
    print("Task 1 is x>3\n"
          "Task 2 is x<=9\n"
          "Task 3 is -4<=x<2")
    while True:
        task = int(input("Input task nr."))
        if task == 1 or task == 2:
            break
    x = float(input("Input point coordinate: "))
    if task == 1:
        isInside_point1(x)
    if task == 2:
        isInside_point2(x)
    if task == 3:
        isInside_point3(x)

__version__ = 1.1
