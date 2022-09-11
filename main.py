import random as r
num = r.randrange(100)
Guess=5 
while Guess>=0 :
    print(Guess)
    your_guess= int(input("enter your guess:\n"))

    def check(x):
        if your_guess==x:
            print ("you win")
        elif your_guess>x:
            print("you r close ,keep trying lower")
        else:
            print("you r close ,keep trying higher")
            return 0
    if Guess>1:
        check(num)
    elif Guess==1:
        check(num)
        print("this is your last chance make the best out if it")
    else:
         print("you lost")
    Guess=Guess -1
    
