# array/list
a = [10, 20, 30, 40, 50]
print(a);

a.insert(5, 80)
print(a)
b = [1, "i", "hello", 10]
print(b)
print(b[2],b[1]);
print(b.index(10));

print("hi" + ' ' + b[2] + ' ' + "are you")
print("Position of hello in varible b is "+str(b.index("hello")))

# tuples
a = (1,2,3)
print(a.count(1));
# set
# dict
d1 = {0:"hi", 2:"hello", "chetan":"welcome"}
print(d1.get(0))
print(d1.get("chetan"));
print(d1.keys())
print(d1.values());

# ------------------------------------------------------------------------------------------------
"""
3 types of data type
1 numerical
2 sequential
3 boolean
"""

a ="intellipaat"
b ="python"
string_c ="intellipaat python training"

print(string_c.count("p"))
y =string_c.replace("training","course")
print(y)

#array/list
a =[10,20,30,40,50]
print(a)

a.insert(5,"hllo")
print(a)
b =[1,"i","hello",20]
print(b)

print(b[2],b[1])
print(b.index(20))


print("hi"+' '+b[2]+' '+"how r u")
print("the position of hello in variable b is "+str(b.index("hello")))

#tuple

a =(1,2,3,7,8,9)
print(a.count(4))

#dictionary
dict1 ={0:"hi",2:"hello","chethan":"welcome"}
print(dict1.get(0))
print(dict1.get("chethan"))
print(dict1.keys())
print(dict1.values())