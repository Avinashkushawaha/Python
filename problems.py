Questions = [
    ["Which language was used to create fb?", "python",
     "French", "Javascript", "Python", "C++", 4]

    ]

for i in range(0, len(Questions)):
    questions = Questions[i][0]
    print("1. ", Questions[i][1])
    print("2. ", Questions[i][2])
    print("3. ", Questions[i][3])
    print("4. ", Questions[i][4])
    answer = int(input("Enter your answer: "))
    if answer == Questions[i][5]:
        print("Correct")
    else:
        print("Incorrect")