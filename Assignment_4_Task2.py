input1 = input("Enter text to write to the file: ")
file1  = open('output.txt', 'w')
file1.write(input1 + "\n")
print("Data successfully written to output.txt.")
file1.close()

input2 = input("Enter additional text to append: ")
file1 = open('output.txt', 'a')
file1.write(input2 + "\n")
print("Data successfully appended.")
file1.close()

file1 = open('output.txt', 'r')
print(file1.read())


