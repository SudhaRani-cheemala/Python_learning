student_score=input("Enter student score inputs\n").split()
for n in range(0,len(student_score)):
    student_score[n] =int(student_score[n])
print(student_score)
print(max(student_score))    
highest_score=0
for score in student_score:
    if score>highest_score:
        highest_score=score
print(f"heightest score is {highest_score}")        

