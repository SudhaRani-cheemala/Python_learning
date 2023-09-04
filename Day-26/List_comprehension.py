numbers=[10,20,30]
new_list=[n+1 for n in numbers]
print(new_list)

name='Angele'
new_list=[letter for letter in  name]
print(name)

# python sequences
#list,range,string,tuple
range_list=[num*2 for num in range(1,5)]
print(range_list)
names=['Alexa','fedore','Deva','Elenor','Freddie']
short_names=[name for name in names if len(name)<5]
print(short_names)
long_names=[name.upper() for name in names if len(name)>5]
print(long_names)
numbers1=[1,2,3,4,5,6,7,]
square_of_numbers=[n1**n1 for n1 in numbers1]
print(square_of_numbers)
numbers2=[1,1,2,4,9,10,89,100000]
odd_list=[n2 for n2 in numbers2 if n2%2==1]
even_list=[n2 for n2 in numbers2 if n2%2==0]
print(even_list)
print(odd_list)

with open('file1.txt') as file1:
    file1_1_data=file1.readlines()
with open('file2.txt') as file2:
    file2_2_data=file2.readlines()
result=[int(num) for num in  file1_1_data if num in file2_2_data]    
print(result)
         
