"""
System to do 6 figure tasks and 3 logical operations.
Author: Edijs Aizgirevičs DP 2-1
"""


def isInside_rec1(x, y):
    """Function,
    to find if given point lies inside a given rectangle or on edge or not.
    Figure coordinates: (-1; 1); (3; 1); (3; -2); (-1; -2)!
    """
    if -1 <= x <= 3 and -2 <= y <= 1:
        if x == -1 or x == 3 or y == -2 or y == 1:
            print("On edge.")
        else:
            print("Inside")
    else:
        print("Outside.")


def isInside_rec2(x, y):
    """Function,
    to find if given point lies inside a given rectangle or on edge or not.
    Figure coordinates: (-5; 3); (2; 3); (2; -1); (-5; -1)!
    """
    if -5 <= x <= 2 and -1 <= y <= 3:
        if x == -5 or x == 2 or y == 1 or y == 3:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_tri(x, y):
    """Function.
    To check whether point P(x, y) lies inside the triangle,
    Figure coordinates: (0; 3); (0; 0); (2; 0)!
    Hypotenuse of the triangle: y = -1.5 * x + 3
    """
    if 0 <= x <= 2 and 0 <= y <= -1.5 * x + 3:
        if x == 0 or y == 0 or y == -1.5 * x + 3:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_cir(x, y):
    """Function.
    To compare radius of circle, with distance of its center from given point.
    Figure coordinates:  R = 1; center (0; 0)!
    """
    if x ** 2 + y ** 2 <= 1 ** 2:
        if x ** 2 + y ** 2 == 1 ** 2:
            print("On edge.")
        else:
            print("Inside")
    else:
        print("Outside")


def isInside_cut_cir(x, y):
    """Function.
    To compare radius of circle, with distance of its center from given point.
    Figure coordinates: center = (-2; 2); R = 1 with cut side y = x + 5
    """
    if ((-2 - x) ** 2 + (2 - y) ** 2) ** 0.5 <= 1 and y <= x + 5:
        if ((-2 - x) ** 2 + (2 - y) ** 2) ** 0.5 == 1 or y == x + 5 and ((-2 - x) ** 2 + (2 - y) ** 2) ** 0.5 < 1:
            print("On edge.")
        else:
            print("Inside")
    else:
        print("Outside")


def isInside_one(x, y):
    """Function.
    To find if given point lies inside a given figure or on edge or not.
    Figure coordinates: (0, 2); (0, -2,5); (-3, -2,5); (-3, 0);
    with cut side y = 2 / 3 * x + 2
    """
    if 0 <= x or x <= -3 and -2.5 >= y or y >= 2 / 3 * x + 2:
        if x == 0 or x == -3 or y == -2.5 or y == 2 / 3 * x + 2:
            print("On edge.")
        else:
            print("Inside.")
    else:
        print("Outside.")


def isInside_point1(x):
    """Function.

    To find if given point lies inside a given interval or not.
    """
    if x > 3:
        print("Inside")
    else:
        print("Not inside")


def isInside_point2(x):
    """Function.

    To find if given point lies inside a given interval or not.
    """
    if x <= 9:
        if x == 9:
            print("On edge.")
        else:
            print("Inside")
    else:
        print("Not inside")


def isInside_point3(x):
    """Function.

    To find if given point lies inside a given interval or not.
    """
    if -4 <= x < 2:
        if x == -4:
            print("On edge.")
        else:
            print("Inside")
    else:
        print("Not inside")


# Driver Code
print("Chose your task type.\n"
      "Type 1 is figure\n"
      "Type 2 is logical operations.")
tipe = float(input("Input type nr."))

if tipe == 1:
    print("Task 1 is rectangle\n"
          "Task 2 is rectangle\n"
          "Task 3 is triangle\n"
          "Task 4 is circle\n"
          "Task 5 is cut circle\n"
          "Task 6 is custom figure")
    task = float(input("Input task nr."))
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
        isInside_one(x, y)

if tipe == 2:
    print("Task 1 is x>3\n"
          "Task 2 is x<=9\n"
          "Task 3 is -4<=x<2")
    task = float(input("Input task nr."))
    x = float(input("Input point coordinate: "))
    if task == 1:
        isInside_point1(x)
    if task == 2:
        isInside_point2(x)
    if task == 3:
        isInside_point3(x)
