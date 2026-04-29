class OddEvenNumberSorter:

    def __init__(self, target_file):
        self.target_file = target_file
        self.even_results = "even.txt"
        self.odd_results = "odd.txt"

        self.color_blue = "\033[94m"
        self.color_green = "\033[92m"
        self.color_yellow = "\033[93m"
        self.text_bold = "\033[1m"
        self.bg_blue = "\033[44m\033[37m"
        self.reset_color = "\033[0m"

    def print_stylish_header(self):
        print(self.bg_blue + "====================================" + self.reset_color)
        print(self.text_bold + "      NUMBER PROCESSING SYSTEM      " + self.reset_color)
        print(self.bg_blue + "====================================" + self.reset_color)

    def sort_the_numbers(self):
        self.print_stylish_header()
        print(f"{self.color_yellow}System: Accessing {self.target_file}...{self.reset_color}")

        try:
            with open(self.target_file, "r") as file_to_read:
                lines_from_file = file_to_read.readlines()

            total_even_count = 0
            total_odd_count = 0

            with open(self.even_results, "w") as even_file, open(self.odd_results, "w") as odd_file:
                for line in lines_from_file:
                    single_number = int(line.strip())

                    if single_number % 2 == 0:
                        even_file.write(str(number_value) + '\n')
                        total_even_count += 1
                    else:
                        odd_file.write(str(number_value) + '\n')
                        total_odd_count += 1

            print(f"{self.text_green}STATUS: OPERATION COMPLETE{self.reset_color}")
            print("-" * 36)
            print(f"RESULT - Even Numbers Saved: {total_even_count}")
            print(f"RESULT - Odd Numbers Saved: {total_odd_count}")
            print("-" * 36)

        except FileNotFoundError:
            print(f"{self.text_bold}\033[91mERROR: File '{self.target_file}' not found.{self.reset_color}")
        except ValueError:
            print(f"{self.text_bold}\033[91mERROR: Non-integer data detected in file.{self.reset_color}")

if __name__ == "__main__":
    my_sorter = OddEvenNumberSorter("numbers.txt")
    my_sorter.sort_the_numbers()