#open file
student_file = open("students.txt", "r")

best_gwa = -1.0
best_student_name = ""

#split student name and gwa
student_name =
student_gwa =

#check gwa if higher
if student_gwa > best_gwa:
    best_gwa = student_gwa
    best_student_name = student_name

student_file.close()

print("The top student is", best_student_name, "with a GWA of", best_gwa)