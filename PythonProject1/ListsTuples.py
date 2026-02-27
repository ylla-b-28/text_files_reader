print ("Enter 5 numbers to arrange the list and find the sum.")
firstNum = input("Enter 1st number: ")
secondNum = input("Enter 2nd number: ")
thirdNum = input("Enter 3rd number: ")
fourthNum = input("Enter 4th number: ")
fifthNum = input("Enter 5th number: ")

sumNum = int(firstNum) + int(secondNum) + int(thirdNum) + int(fourthNum) + int(fifthNum)
totalNum = firstNum + secondNum + thirdNum + fourthNum + fifthNum

listNum = list(totalNum)
sortedNum = sorted(listNum)

print ("Enter 5 numbers: " + totalNum)
print ("Sorted numbers: " + sortedNum)
print ("Sum of the 5 numbers: " + sumNum)


    