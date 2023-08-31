file=open('my_file.txt')
contents=file.read()
print(contents) 
file.close()
# w stands for write
with open("my_file.txt",mode="w") as file2:
    file2.write("Hello  iam xyz from Hyderabad + "" + jkasjdfhjfadhf")
# a stands for append a data to existing data
with open("my_file.txt",mode="a") as file3:
    file3.write("\nAppended a text")
    # it has been created a new text file with some data 
with open("new_file.txt",mode="w") as file1:
    file1.write("new file created through this")  
with open("/Users/sudharani.ch/OneDrive - FPT Software/Desktop/Python_Learning/Python_learning/Day-24/my_file.txt") as file5:
    contents=file5.read()
    print(contents)            
with open("../../Desktop/Python_Learning/Python_learning/Day-24/my_file.txt") as file6:
    con=file6.read()
    print(con)    