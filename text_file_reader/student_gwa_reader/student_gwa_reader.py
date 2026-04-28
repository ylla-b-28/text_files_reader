class StudentGwaReader:

    def __init__(self, record_file):
        self.record_file = record_file

        self.text_bold = "\033[1m"
        self.text_cyan = "\033[96m"
        self.text_green = "\033[92m"
        self.bg_black_white = "\033[40m\033[37m"
        self.reset = "\033[0m"

    def print_banner(self):
        print(self.bg_black_white + "====================================" + self.reset)
        print(self.text_bold + "     ACADEMIC RECORD ANALYZER       " + self.reset)
        print(self.bg_black_white + "====================================" + self.reset)

    def find_highest_gwa(self):
        self.print_banner()

        best_gwa = -1.0
        best_student_name = ""

try:
    print(f"{self.text_cyan}Status: Accessing records from {self.record_file}...{self.reset}")

    with open(self.record_file, "r") as source_data:
        for line in source_data:
            if not line.strip():
                continue

            parts = line.strip().rsplit(",", 1)

            if len(parts) == 2:
               student_name = parts[0].strip()
               student_gwa = parts[1].strip()

               if student_gwa > best_gwa:
                    best_gwa = student_gwa
                    best_student_name = student_name

    if top_student_name:
        print("-" * 36)
        print(f"{self.text_green}ANALYSIS COMPLETE{self.reset}")
        print(f"The highest GWA was achieved by:")
        print(f"{self.text_bold}{top_student_name}{self.reset}")
        print(f"Final GWA: {highest_gwa_value}")
        print("-" * 36)
    else:
        print("No student records found in the file.")

    except FileNotFoundError:
        print(f"{self.text_bold}\033[91mERROR: '{self.record_file}' not found.{self.reset}")
    except ValueError:
        print(f"{self.text_bold}\033[91mERROR: Data format error (GWA must be numeric).{self.reset}")

if __name__ == "__main__":
    tracker_instance = AcademicTracker("students.txt")
    tracker_instance.find_top_performer()