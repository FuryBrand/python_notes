def make_the_pizza(size, *toppings):
    """
    概述要制作的比萨
    供lesson01_08-09.py使用
    """
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)