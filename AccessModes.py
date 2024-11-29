#reading the file
file = open('text.txt', 'r')
print("File in read mode!\n")
print(file.read())
file.close()

#overwriting the file
file = open('text.txt', 'w')
file.write("File in the write mode.....\n")
file.write("Hello I am Arshabh!\n")
file.close()

#appending to the file
file = open('text.txt', 'a')
file.write("File in the append mode.....\n")
file.write("Hello World\n")
file.close()

#reading multiple lines
file = open('text.txt','r')
print("Reading multiple lines...\n")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#iterating over the file
file = open('text.txt','r')
print("Looping through the lines...\n")
for line in file:
  print(line)
file.close()

#splitting words
with open('Codingal.txt', 'w') as file:
  file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

with open('Codingal.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")

for line in data:
    word = line.split()
    print(word)
file.close()
