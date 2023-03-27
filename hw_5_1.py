text = input("Text the message -> ")
chars = list(text)
for char in chars:
    if char.isdigit():
        if int(char) % 2 == 0:
            print(f"{char} is an even number")
        else:
            print(f"{char} is an odd number")
    elif char.isalpha():
        if char.isupper():
            print(f"{char} is an upper letter")
        else:
            print(f"{char} is an lower letter")
    else:
        print(f"{char} is a symbol")