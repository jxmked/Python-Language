import os

border = "*~*-*~*-*~*-*~*-*~*-*~*-*~*-*~*"

def Confirm(s):
    r = ""
    while True:
        x = input("\n{} [Y/n]: ".format(s))
        
        if len(x) == 0:
            continue
        
        x = x[0]
        
        if x == "y" or x == "Y":
            return True
        
        if x == "n" or x == "N":
            return False
       
def clrscr():
    os.system("clear")

def displayMenu(arr):
    l = len(arr)
    
    print(border)
    
    for i in range(0, l):
        print("{}. {}".format(i + 1, arr[i]))
        
    print(border)
    
    ans = ""
    while True:
        ans = input("Which number: ")
        
        if len(ans) == 0:
            continue
        
        try:
            res = int(ans)
            
            if res < l and res > 0:
                return res
        except:
            pass

def Scale(question, n, x):
    # n = Min
    # x = Max
    
    print(question)
    
    while True:
        res = input("Number {}-{}: ".format(n, x))
        
        if len(res) == 0:
            continue
        
        try:
            res = int(res)
            
            if res >= n and res <= x:
                return res
        except:
            pass

# Start Here
def Main():
    clrscr()
    
    print(border)
    print("WELCOME TO IME!!\n")
    print("Hi! This program will assess the condition of your mental health.")
    print("Question will be ask as you go through the program.")
    print("IME will provide recommendations depending on the result of your assessment.")
    print(border)
    
    if Confirm("Do you want to continue?"):
        clrscr()
        print("Did you know that Mental Health includes our emotional, psychological, and social well-being.")
        print("It affects how we think, feel, and act. It also helps determine how we handle stress, relate to others, and make choices.")
        print("Mental health is important at every stage of life, from childhood and adolescence through adulthood.")
        
        FirstPage()
        # Next Function
    else:
        clrscr()
        print("\nThank you for visiting IME program!" )
        exit(0)


def FirstPage():
    
    if Confirm("Do you want to test yourself?"):
        # Want to test
        clrscr()
        print("Select Mental Health Assessment")
        
        selections = [
            "Stress Assessment",
            "Depression Assessment",
            "Anxiety Assessment",
            "Back"
        ]
        
        ans = displayMenu(selections)
        
        
        if ans == 1: # Stress Assessment
            if Confirm("Feeling unoveewhelmed, unmotivated or unfocused?"):
                StressAssessment()
            else:
                pass
        
        if ans == 2: # Depression Assessment
            pass
        
        if ans == 3: # Anxiety Assessment
            pass 
        
        if ans == 4: # Back
            Main()
        
    
def StressAssessment():
    clrscr()
    
    print("Rate the following qustions by using this option.")
    print("\n0 = Not at all")
    print("1 = Several Day")
    print("2 = More than half days")
    print("3 = Nearly Everyday")
    print(border)
    
    questions = [
        "Feeling unoverwhelmed, unmotivated, or unfocused",
        "Trouble sleeping or sleeping too much",
        "Racing thoughts or constant worry",
        "Problems with your memory or concentration",
        "Making bad decisions",
        "I feel I am left with hardly anytime for exercise",
        "I feel tired",
        "I have gained/lost weight",
        "I am tired and sleeping more/less than normal",
        "Feeling of being left alone"
    ]
    
    result = 0
    
    for i in range(0, len(questions)):
        print("")
        result += Scale("{}. {}".format(i + 1, questions[i]), 0, 3)
       
     
    print(border, "\n", result)
    if result <= 6 :
        print("Normal or No Problem with Stress")
        
    elif result >= 7 and result <= 11 :
        print("Mild Stress")
        
    elif result >= 12 and result <= 20 :
        print("Moderate Stress")
        
    else:
        print("Severe Stress")
    

# Must be at the bottom
Main()
