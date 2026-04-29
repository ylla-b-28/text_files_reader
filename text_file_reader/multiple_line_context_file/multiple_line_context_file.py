def record_life_lines():
    filename = "mylife.txt"

    with open(filename, "a") as diary_file:
        active = True

        while active:
            user_input = input("Enter line: ")
            diary_file.write(user_input + "\n")

            choice = input("Are there more lines y/n? ").lower()
            if choice == "n":
                active = False

record_life_lines()