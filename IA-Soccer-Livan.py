ai = 'Livan'
n=0
print ('Welcome to a artifical inteligence about football')
print ('Do you know anything about football?')
print ('y/n:')
level=input()
if level == 'y': 
    print ("Then let me ask you some questions")
    print ("What is your name?")
    name=input()
    print ("Nice to meet you {}".format(name), "I'm Livan")
    print ("Can you tell me in which year was the first mundial played?")
    year=input()
    if year=="1930":
        n=n+1
        print ("Correct answer! Do you know when FC Barcelona was created?")
        fc=input()
        if fc =="1899":
            n=n+1
            print("The last question is hard.  What is the name of the german league?")
            german=input()
            if german=="bundesliga":
                n=n+1
                print("Wow, you reached a level {}".format(n) , "You are a master!")
            else:
                print ("I think you are not prepared for this, sorry")
                print ("Goodbye")          
        else:
            print("Wrong. The last question is hard.  What is the name of the german league?")
            german=input()
            if german=="bundesliga" or "Bundesliga":
                n=n+1
                print("You reached a level {}".format(n))
            else:
                print ("I think you are not prepared for this, sorry")
                print ("Goodbye")
    else:
        print ("Wrong answer, it was on 1930. Do you know when FC Barcelona was created?")
        fc=input()
        if fc =="1899":
            n=n+1
            print("The last question is hard.  What is the name of the german league?")
            german=input()
            if german=="bundesliga":
                n=n+1
                print("Wow, you reached a level {}".format(n) , "You are a master!")
            else:
                print ("I think you are not prepared for this, sorry")
                print ("Goodbye")          
        else:
            print("Wrong. The last question is hard.  What is the name of the german league?")
            german=input()
            if german=="bundesliga" or "Bundesliga":
                n=n+1
                print("You reached a level {}".format(n))
            else:
                print ("I think you are not prepared for this, sorry")
                print ("Goodbye")
       
else: 
    print ("Then I think you are not prepared for this, sorry")
    print ("Goodbye")