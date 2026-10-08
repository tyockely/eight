while True:
    choice = input("Choose a number")
    for i in range(int(choice)):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
    break