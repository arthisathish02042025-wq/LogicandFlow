# Calculate the student grade on marks in 3 subjects

Student_name = input("Student name:")
Subject1 = float(input("Subject1 marks:"))
Subject2 = float(input("Subject2 marks:"))
Subject3 = float(input("Subject3 marks:"))

# Calculate
Total_marks = Subject1 + Subject2 + Subject3
print(f"Total_marks: {Total_marks}")
Percentage = (Total_marks / 300) * 100
print(f"Percentage scored:{Percentage}%")

#Grade Logic
if Percentage >= 75:
    print("Grade: A")
elif Percentage >= 60 and Percentage < 75:
    print("Grade: B")
elif Percentage >= 40 and Percentage < 60:
    print("Grade: C")
elif Percentage < 40:
    print("Grade:F")
else:
    print("Invalid data")
 
