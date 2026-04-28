def separate_even_and_odd(file_to_read):
    with open(file_to_read, 'r')  as source_file:
        number_data = source_file.readlines()

#open the file
with open ('even.txt', 'w') as even_file, open ('odd.txt', 'w') as odd_file:
#read every line
    for line in number_data:
        number_value = int(line.strip())

    if number_value % 2 == 0:
        even_file.write(str(number_value) + '\n')
    else:
        odd_file.write(str(number_value) + '\n')

separate_even_and_odd("numbers.txt")
print("Files have been updated!")