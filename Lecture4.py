VOWLES = ("a", "i", "u", "e", "o")

message = input("Enter your message : ").lower().strip()

new_message = ""


for letter in message:
    if letter not in VOWLES:
        new_message += letter
        
print(new_message)