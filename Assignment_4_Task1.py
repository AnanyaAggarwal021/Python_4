try:
    file_check = open('sample.txt', 'r')
    readingFile = file_check.readlines()
    for i in range(len(readingFile)):
        print("Line", i + 1, ":", readingFile[i].strip())
    file_check.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
