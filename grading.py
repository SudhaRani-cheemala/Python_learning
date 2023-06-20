students_scores={"harry":81,"smith":45,"snigdha":98,"hima":86,"jashua":38}
student_grades={}
for student in students_scores:
    # print(student)
    score=students_scores[student]
    if score > 90:
        student_grades[student]="Outstanding"
    elif score>80:
        student_grades[student]="Exceeds expectations"    
    elif score >70:
        student_grades[student]="Average"
    else:
        student_grades[student]="fail"        
print(student_grades)        