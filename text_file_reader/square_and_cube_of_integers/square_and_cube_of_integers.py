class IntegerProcessor:
    def __init__(self, source_file):
        self.source_file = source_file

        self.blue = "\033[94m"
        self.green = "\033[92m"
        self.bold = "\033[1m"
        self.reset = "\033[0m"

    def separate_and_calculate(self):
        print(f"{self.blue}Status: Processing {self.source_file}...{self.reset}")

        try:
            with open(self.source_file, "r") as main_data, \
                 open("double.txt", "w") as even_file, \
                 open("triple.txt", "w") as odd_file:

                for entry in main_data:
                    clean_entry = entry.strip()
                    if not clean_entry:
                        continue

                    number = int(clean_entry)
                    if number % 2 == 0:
                        even_file.write(f"{number ** 2}\n")
                    else:
                        odd_file.write(f"{number**3}\n")

            print(f"{self.green}{self.bold}Success! Files 'double.txt' and 'triple.txt' are ready.{self.reset}")

        except FileNotFoundError:
            print(f"\033[91mError: Missing source file.{self.reset}")
        except ValueError:
            print(f"\033[91mError: File contains invalid characters.{self.reset}")

if __name__ == "__main__":
    app_name = IntegerProcessor("integers.txt")
    app_name.separate_and_calculate()
