# Open function to open the file "MyFile1.txt" (same directory) in append mode and
#file1 = open("MyFile1.txt","a")
#file1.close()
file1 = open("MyFile1.txt","w+")

#write a string to file MyFile1.txt
#s = "Hello\n"
#file1.write(s)

#file1.close()

file1 = open("MyFile1.txt","r")
print(file1.read())
file1.close()

file1 = open("MyFile1.txt","w")
L = ["This is sparta\n", "This is richard\n"]
file1.writelines(L)
file1.close()

file1 = open("MyFile1.txt", "a") #append mode
file1.write("Hello\n")  
file1.close()

file1 = open("MyFile1.txt", "r") #read mode
print("Output before append")
print(file1.read())
print()
file1.close()

