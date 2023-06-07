first=input("Enter first person name")
print(first)
second=input("Enter 2nd person name")
print(second)
combined_string=first+second
lower_string=combined_string.lower()
t=lower_string.count("t")
r=lower_string.count("r")
u=lower_string.count("u")
e=lower_string.count("e")
true=t+r+u+e
l=lower_string.count("l")
o=lower_string.count("o")
v=lower_string.count("v")
e=lower_string.count("e")
love=l+o+v+e
love_score=str(love)+str(true)
print(f"Your love score is {love_score}")