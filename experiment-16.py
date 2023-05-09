# Write a program to...
# i) To open a file in read mode and write its contents to another file but replace every occurrence of character ‘h’
file1 = open("test.txt",'r')
s=file1.read()
s = s.replace("h", "x" ) 
file1.close()

file1=open("test.txt","w")
file1.write(s)
file1.close()

file1 = open("test.txt", "r")
print("Contents of File after Replacing: ")
for x in file1.readlines():
	print(x,end='')
print()

# ii) To open a file in read mode and print the number of occurrences of a character ‘a’.
file1 = open("test.txt",'r')
s=file1.read()
counter = s.count("a")
file1.close()
print("No.of occurrences of a character ‘a’ in File text.txt is: "+str(counter))