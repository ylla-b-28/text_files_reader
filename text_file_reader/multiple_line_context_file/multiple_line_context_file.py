#write a file
f = open("mylife.txt", "w")
#enter line
more = "y"
while more == "y":
    line = input("Enter line: ")
    f.write(line + "\n")
#question
    more = input("Are there more lines y/n? ")
#close
f.close()