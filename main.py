# Ask the user for their age
age = int(input("Enter your age: "))

# Check the age and give a response
if age < 18:
    print("You are a a Child/Teenager .")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
