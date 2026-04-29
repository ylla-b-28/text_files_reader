class StudentGwaReader:

    def __init__(self, record_file):
        self.record_file = record_file

        self.text_bold = "\033[1m"
        self.text_cyan = "\033[96m"
        self.text_green = "\033[92m"
        self.color_yellow = "\033[93m"
        self.reset = "\033[0m"

    def print_banner(self):
        print(self.text_green + "====================================" + self.reset)
        print(self.color_yellow + "     ACADEMIC RECORD ANALYZER       " + self.reset)
        print(self.text_green + "====================================" + self.reset)

    def find_highest_gwa(self):
        self.print_banner()

        best_gwa = 5.1
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
                    student_gwa = float(parts[1].strip())

                 if student_gwa < best_gwa:
                    best_gwa = student_gwa
                    best_student_name = student_name

            if best_student_name:
                print("-" * 36)
                print(f"{self.text_green}ANALYSIS COMPLETE{self.reset}")
                print(f"The highest GWA was achieved by:")
                print(f"{self.text_bold}{best_student_name}{self.reset}")
                print(f"Final GWA: {best_gwa}")
                print("-" * 36)
            else:
                print("No student records found in the file.")

        except FileNotFoundError:
           print(f"{self.text_bold}\033[91mERROR: '{self.record_file}' not found.{self.reset}")
        except ValueError:
           print(f"{self.text_bold}\033[91mERROR: Data format error (GWA must be numeric).{self.reset}")

if __name__ == "__main__":
    tracker_instance = StudentGwaReader("students.txt")
    tracker_instance.find_highest_gwa()