# import random
# student_scores={student:random.randint(1,100) for student in names}
# passed_students={student:score for (student,score) in student_scores.dictionary.items()}
sentence="What is the Airspaced velocity of an unladen swallow?"
result={word:len(word) for word in sentence.split()}
print(result)
weather_c={
"Monday":12,
"Tuesday":12,
"Wednesday":12,
"Thursday":12,
"Friday":12,
  
    
}
weather_f={day:(temp_c*9/5)+32 for (day,temp_c) in weather_c.items()}
print(weather_f)