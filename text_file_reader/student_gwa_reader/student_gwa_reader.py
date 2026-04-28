def find_highest_gwa(filename):
    best_gwa = -1.0
    best_student_name = ""

try:
    with open(filename, "r") as input_file:
        for current_line in input_file:
            if not current_line.strip():
                continue

            data = current_line.strip().rsplit(",", 1)

            if len(data) == 2:
               student_name = data[0].strip()
               student_gwa = data[1].strip()

               if student_gwa > best_gwa:
                    best_gwa = student_gwa
                    best_student_name = student_name

    if best_student_name:
        print(f"Top Performer: {best_student_name} ({best_gwa})")

except FileNotFoundError:
        print("Error: students.txt not found.")
except ValueError:
        print("Error: Found a grade that isn't a number.")

find_highest_gwa("students.txt")