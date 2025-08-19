try:
    f = open("sample.txt", "r")
    text = f.read()
    print(text)
    f.close()
except FileNotFoundError:
    print("File not found")


# task2

name = input("Enter your name: ")
f = open("output.txt", "w")
f.write(name)


with open("output.txt", "a") as file:
    file.write(" This is new content.\n")