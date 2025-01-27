from random import randint
num = randint(0, 10)
num_for_people = int(input("Яке це число на вашу думку від 0 до 10? "))

if num_for_people < num:
    print("Ваше число замале")
    num_for_people = int(input("Яке це число на вашу думку? "))
    if num_for_people < num:
        print("Ваше число замале")
        num_for_people = int(input("Яке це число на вашу думку? "))
        if num_for_people < num:
            print("Ваше число замале")
            print(f"Число було: {num}")
        elif num_for_people > num:
            print("Ваше число завелике")
            print(f"Число було: {num}")
        elif num_for_people == num:
            print("Ви вгадали!")
    elif num_for_people > num:
        print("Ваше число завелике")
        num_for_people = int(input("Яке це число на вашу думку? "))
        if num_for_people < num:
            print("Ваше число замале")
            print(f"Число було: {num}")
        elif num_for_people > num:
            print("Ваше число завелике")
            print(f"Число було: {num}")
        elif num_for_people == num:
            print("Ви вгадали!")
    elif num_for_people == num:
        print("Ви вгадали!")
elif num_for_people > num:
    print("Ваше число завелике")
    num_for_people = int(input("Яке це число на вашу думку? "))
    if num_for_people < num:
        print("Ваше число замале")
        num_for_people = int(input("Яке це число на вашу думку? "))
        if num_for_people < num:
            print("Ваше число замале")
            print(f"Число було: {num}")
        elif num_for_people > num:
            print("Ваше число завелике")
            print(f"Число було: {num}")
        elif num_for_people == num:
            print("Ви вгадали!")
    elif num_for_people > num:
        print("Ваше число завелике")
        num_for_people = int(input("Яке це число на вашу думку? "))
        if num_for_people < num:
            print("Ваше число замале")
            print(f"Число було: {num}")
        elif num_for_people > num:
            print("Ваше число завелике")
            print(f"Число було: {num}")
        elif num_for_people == num:
            print("Ви вгадали!")
    elif num_for_people == num:
        print("Ви вгадали!")
elif num_for_people == num:
    print("Ви вгадали!")
