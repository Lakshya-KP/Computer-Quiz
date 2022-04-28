print("Welcome to my computer quiz!")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    print("Goodbye!")
    quit()

print("Okay! Let's Play :)")
marks=0

answer = input("What does C.P.U stand for?\n")
if answer.lower() == "central processing unit":
    print("Correct!")
    marks += 1
else: print("Incorrect!")

answer = input("What does G.P.U stand for?\n")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    marks += 1
else: print("Incorrect!")

answer = input("What does RAM stand for?\n")
if answer.lower() == "random access memory":
    print("Correct!")
    marks += 1
else: print("Incorrect!")

answer = input("What does PSU stand for?\n")
if answer.lower() == "power supply unit":
    print("Correct!")
    marks += 1
else: print("Incorrect!")

print("\nQuiz Finished!\nThank you for particpating.\nyou got",marks,"questions correct.")
print("you scored",(marks/4)*100,"%")