def name_age():
    print("Type in your name")
    x = input()
    print("Type in your age")
    y = input()

    print("Hello " + x + ". Your age is: " + y)


    return

def name_age_2():
    print("Type in your name")
    x = input()
    print("Type in your age")
    y = input()

    print(x+y)
    return


def swap_integers(num1, num2):
    x = num1
    y = num2

    print(f'X={x}')
    print(f'Y={y}')

    x = num2
    y = num1

    print(f'X={x}')
    print(f'Y={y}')

    print(f'{x}'+f'{y}')
    return

def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0):
        if (num1 % 10 == 0 and num2 % 10 == 0):
            return True
        else:
            return False

    return False


def sum_up(num1, num2):

    if (num1 > num2):

        return 0

    if (num1 < 0 or num2 < 0):

        return 0

    y = 0
    for x in range (num1, num2+1):
        y = y + x

    return y


def circle_area(r1, r2, r3):

  x = r1*r1*3.141
  y = r2*r2*3.141
  z = r3*r3*3.141

  return x + y +z


def check_string(text):
    if text.startswith("a") or text.startswith("A") or text.endswith("a"):
        return True
    else:
        return False

def triangle(rows):
    for i in range(rows):
        x = "*"
        for q in range(i):
            x = x + "*"
        print(x)



















