print("\033[1mBRIZA, Pryllanie Kirsten\033[0m")
print("BSCpE 1-4 | CMPE 102 \n")

print("\033[1mResume\033[0m \n")

surname = input("Kindly enter your surname: ")
name = "Name: Pryllanie Kirsten A. Briza\n"
objective = "Objective: Eager to apply my skills in programming and problem-solving within a dynamic team environment.\n"
personal = "Personal Background:\nAge: 18 \nBirthday: December 28, 2006\nAddress: Almanza Uno, Las Piñas City\n"

educational = "Educational Background: \nCollege: Polytechnic University of the Philippines - Main\nHigh School: Las Piñas City National Senior High School - Doña Josefa Campus \nElementary: Our Lady of the Abandoned Catholic School \n"

skills = "Skills: \nTechnical Skills: Microsoft Apps, HTML, CSS, Java \nCertifications: TESDA National Certificate II in Computer System Servicing \nLanguages: English, Filipino \nInterests: Reading online books, listening to musics, baking desserts, playing online game \n"

achievements = "Achievements: \nLAS PIÑAS CITY NATIONAL SENIOR HIGH SCHOOL - DOÑA JOSEFA CAMPUS \nMost Outstanding Girl Scout of the Year \nMayor Nene Aguilar Academic Excellence Award \nDoña Josefa Campus ICT Club Excellence Award \nWith High Honors - Grade 12 \nOverall Best in Science (Earth and Life Science & Physical Science) \nOverall Best in TVL-ICT (Animation NCII & Programming) \nOverall Best in Filipino \nOverall Best in Research in ICT \nFirst Place - Scientific Investigatory Project \nSecond Place - Oratorical Speech \nWith High Honors - Grade 11 \nGirl Scout of the Philippines Awardee \n\nCENTRO ESCOLAR LAS PIÑAS \nWith High Honors - Grade 10 \nWith High Honors - Grade 9  \nWith High Honors - Grade 8 \n\nSAN BEDA COLLEGE ALABANG \nSt. Maur Awardee - Grade 7 \n"

reference = "Character Reference: Mr. Micheal G. Mesa - micheal.mesa@deped.gov.ph"

print("\n")

print("This is the resume of: " + surname)
print(name)
print(objective)
print(personal)
print(educational)
print(skills)
print(achievements)
print(reference)

print("\n")

print("\033[1mBasic Calculator\033[0m \n")

firstNum = int(input("Please input your first number: "))
secondNum = int(input("Please input your second number: "))

print("Answers: \n")

add = firstNum + secondNum
sub = firstNum - secondNum
mul = firstNum * secondNum
div = firstNum / secondNum
mod = firstNum % secondNum
exp = firstNum ** secondNum

print("Add: " + str(firstNum) + " + " + str(secondNum) + " = " + str(add))
print("Subtract: " + str(firstNum) + " - " + str(secondNum) + " = " + str(sub))
print("Multiply: " + str(firstNum) + " * " + str(secondNum) + " = " + str(mul))
print("Divide: " + str(firstNum) + " / " + str(secondNum) + " = " + str(div))
print("Modulus: " + str(firstNum) + " % " + str(secondNum) + " = " + str(mod))
print("Exponent: " + str(firstNum) + " ** " + str(secondNum) + " = " + str(exp))