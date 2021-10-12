#!/usr/bin/python3

# CYSA Exam Questions!

#import time 


Welcome = input("Welcome to Cysa+ Exam Questions!\nThere will be 10 questions.\nPress Y to continue\n\nGoodluck\n\n")
print(" ")
while Welcome == "y":

    print("""After running an nmap scan of a system, you receive scan data that indicates the following 
                three ports are open:\n
                22/TCP
                443/TCP
                1521/TCP\n
                What services commonly run on these ports?\n\n               
                1. SMTP, NetBIOS, MySQL
                2. SSH, Microsoft DS, WINS
                3. SSH, HTTPS, Oracle
                4. FTP, HTTPS, MS-SQL\n""")
#time.sleep(3)

    Answers1 = {

        "SMTP, NetBIOS, MySQL" : "1", 
        "SSH, Microsoft DS, WINS" : "2", 
        "SSH, HTTPS, Oracle" : "3", 
        "FTP, HTTPS, MS-SQL" : "4"
    }

    List1 = list(Answers1.keys()) #turns words into a list
    
    correct = 0
    wrong = 0 
    for keyword in List1:
        display = "{}"

        print(display.format(keyword))
        userInputAnswer = input("\nWHAT IS THE ANSWER?\n: ")
        print(userInputAnswer)
        print(Answers1[keyword])
        print(" ")

    if userInputAnswer == (Answers1[keyword]):
        print("CORRECT")
        correct += 1
    else:
        print("WRONG")
        wrong += 1
    print("_"*25)
        
    # final score
    displayScore = "SCORE: {} correct and {} wrong"
    print(displayScore.format(correct, wrong))
    Welcome = input("Play again? ('y' to continue) ")
print(" ")
print("Thanks for playing")