from random import choice

response = input("options: ")
options = response.split(",")
selected = choice(options)
print(f"Selected: {selected}")
options.remove(selected)

while True:
    response = input("Enter 'exit' to quit and anything else to continue: ")
    if response.lower() == 'exit':
        break

    if options:
        selected = choice(options)
        print(f"Selected: {selected}")
        options.remove(selected)
    else:
        print("No more options to choose from.")
        break

