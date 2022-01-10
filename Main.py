file = open("test1.txt", "r")
content = file.read()
content = content.split("\n")
file.close()

dictionary = {}

for i in content:
    dictionary[i] = len(i)

print(dictionary)

file = open("test1.txt", "w")
file.writelines(str(dictionary))
file.close()