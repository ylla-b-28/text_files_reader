grade = eval(input("Enter grade: "))
if grade < 0:
    print("Invalid grade. Grade must be greater than 0.")
elif grade >= 75:
    print("PASS")
else:
    print("FAIL")


    