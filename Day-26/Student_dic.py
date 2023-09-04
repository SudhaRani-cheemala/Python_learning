student_dic={
    "student":["Angela","James","Lilly"],
    "Score":[56,78,49]   
}
for (key,value) in student_dic.items():
     print(value)
import pandas
student_data_frame=pandas.DataFrame(student_dic)
print(student_data_frame)     
# Loop through dataframe
for (index,row) in student_data_frame.iterrow():
    if row.student == "Angela":
        print(row.score)