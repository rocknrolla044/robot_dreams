text = input("Text the message -> ")

if text.isdigit():
    if int(text) % 2 == 0:
        print("Your message is an even number.")
    else:
        print("Your message is an odd number.")

elif text.isalpha():
    print(f"Your message is a word with {len(text)} letters")
else:
    print("Try to type another message.")
