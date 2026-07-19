file = open("sample.txt", "w")
file.write("Hello, GitHub!")
file.close()

file = open("sample.txt", "r")
print(file.read())
file.close()
