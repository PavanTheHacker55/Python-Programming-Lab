# File Input/output: Write a program to
# i) To create simple file and write “Hello World” in it.
file1 = open("myfile.txt", "w")
s = "Hello World"
file1.writelines(s)
file1.close()
# Reading...
file1 = open("myfile.txt", "r")
print("Contents of File Before Appeding: "+file1.read())
file1.close()

# ii) To open a file in write mode and append Hello world at the end of a file.
file1 = open("myfile.txt", "a") # append mode
file1.write(" Hello World")
file1.close()
# Reading...
file1 = open("myfile.txt", "r")
print("Contents of File After Appeding: "+file1.read())
file1.close()
