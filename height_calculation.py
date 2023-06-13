student_heights=input("Input a list of students heights\n").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(f"student height is {student_heights}")    
total_height=0
for height in student_heights:
  total_height+=height
print(f" total height of the  student {total_height}")
number_students=0
for student in student_heights:
   number_students+=1
print(f" number of students are {number_students}")   
avg_height=round(total_height/number_students)
print(f"average height of the student {avg_height}")  