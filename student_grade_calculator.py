name=input("Enter student name: ")
while True:
    math=int(input("Enter Math marks: "))
    if 1 <= math <= 100:
        break
    else:
        print("An Invalid Marks! Please enter marks  between 1 and 100.")

while True:
    english=int(input("Enter English marks: "))
    if 1 <= english <= 100:
        break
    else:
        print("An Invalid Marks! Please enter marks  between 1 and 100.")

while True:
    python=int(input("Enter Python marks: "))
    if 1 <= python <= 100:
        break
    else:
        print("An Invalid Marks! Please enter marks  between 1 and 100.")

total_marks = math + english + python
average_marks = total_marks / 3

print(f"Student Name: {name}")
print(f"Average Marks: {average_marks:.2f}")

if average_marks >= 80 and average_marks <= 100:
    print("Final Grade: A+")
elif average_marks >= 70 and average_marks < 80:
    print("Final Grade: A")
elif average_marks >= 60 and average_marks < 70:    
    print("Final Grade: B")
elif average_marks >= 50 and average_marks < 60:
    print("Final Grade: C")
# elif average_marks >= 40 and average_marks < 50:
#     print("Final Grade: C")
else:
    print("Final Grade: F")