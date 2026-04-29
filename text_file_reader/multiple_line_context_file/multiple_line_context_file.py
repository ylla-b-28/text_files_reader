class MultiLineWriter:

    def __init__(self, target_filename):
        self.target_filename = target_filename

        self.purple_color = "\033[95m"
        self.green_color = "\033[92m"
        self.bold = "\033[1m"
        self.reset = "\033[0m"

    def run_writer(self):
        print(f"{self.purple_color}{self.bold}--- MY LIFE WRITER SYSTEM ---{self.reset}")

        try:
            with open(self.target_filename, "a") as output_file:
              is_running = True

              while is_running:
               line_to_save = input("Enter line: ")
               output_file.write(line_to_save + "\n")

               user_choice = input("Are there more lines y/n? ").lower()

               if user_choice == 'n':
                   is_running = False

        except IOError:
            print(f"\033[91mError: Could not access {self.target_filename}{self.reset}")

if __name__ == "__main__":
    writer_instance = MultiLineWriter("mylife.txt")

    writer_instance.run_writer()