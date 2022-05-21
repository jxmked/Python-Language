import os

border = "========================="

def Confirm(s):
    while True:
        # While User Keeps Entering Invalid Input
        # Keep Asking The User Until we Get the expected Input
        x = input("\n{} [Y/n]: ".format(s))
        
        # Check if user entered something
        if len(x) == 0:
            continue
        
        # Get the first Character from string
        x = x[0]
        
        # Check if User Input Met our Condition
        if x == "y" or x == "Y":
            return True
        
        if x == "n" or x == "N":
            return False
       
def clrscr():
    os.system("clear")

def displayMenu(arr):
    num = len(arr) # Length of an Array
    
    border = "*~*-*~*-*~*-*~*-*~*-*~*-*~*-*~*"
    
    print(border)
    
    # Print each Value From Array after a Number
    for i in range(0, num):
        # This line is Equivalent to `printf("%d. %s", i + 1, arr[i])` in C language
        print("{}. {}".format(i + 1, arr[i]))
        
    print(border)
    
    while True:
        # While User Keeps Entering Invalid Input
        # Keep Asking The User Until we Get the expected Input
        
        ans = input("Which number: ")
        
        # Check if user entered something
        if len(ans) == 0:
            continue
        
        try: 
            # Since `int` functiin will `raise` (call) an error by passing an invalid character
            # We can handle it by using `try-except` method
            ans = int(ans)
            
            # Check if User Input Met our Condition
            if ans < num and ans > 0:
                return ans
        except:
            # `pass` means "No operation".
            pass

def Scale(question, n, x):
    # n = Min
    # x = Max
    
    print(question)
    
    while True:
        # While User Keeps Entering Invalid Input
        # Keep Asking The User Until we Get the expected Input
        
        # This line is Equivalent to `printf("Number %d-%d", n, x)` in C language
        ans = input("Number {}-{}: ".format(n, x))
        
        # Check if user entered something
        if len(ans) == 0:
            continue
        
        try:
            # Since `int` functiin will `raise` (call) an error by passing an invalid character
            # We can handle it by using `try-except` method
            ans = int(ans)
            
            # Check if User Input Met our Condition
            if ans >= n and ans <= x:
                return ans
        except:
            # `pass` means "No operation".
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
        print(border)
        print("Did you know that Mental Health includes our emotional, psychological, and social well-being.")
        print("It affects how we think, feel, and act. It also helps determine how we handle stress, relate to others, and make choices.")
        print("Mental health is important at every stage of life, from childhood and adolescence through adulthood.")
        print(border)
        
        FirstPage()
    else:
        clrscr()
        print("\nThank you for visiting IME program!" )
        exit(0)

def FirstPage():
    if Confirm("Do you want to test yourself?"):
        # Want to test
        clrscr()
        print("Select Mental Health Assessment")
        
        ans = displayMenu([
            "Stress Assessment",
            "Depression Assessment",
            "Anxiety Assessment",
            "Back"
        ])
        
        if ans == 1: # Stress Assessment
            clrscr()
            
            if Confirm("Feeling unoveewhelmed, unmotivated or unfocused?"):
                StressAssessment()
            else:
                # `pass` means "No operation".
                pass
        
        if ans == 2: # Depression Assessment
            # `pass` means "No operation".
            pass
        
        if ans == 3: # Anxiety Assessment
            # `pass` means "No operation".
            pass 
        
        if ans == 4: # Back
            Main()
        
    
def StressAssessment():
    clrscr()
    
    print("Rate the following qustions by using this option.\n")
    print("0 = Not at all")
    print("1 = Several Day")
    print("2 = More than half days")
    print("3 = Nearly Everyday")
    print(border)
    
    questions = [
        "Feeling unoverwhelmed, unmotivated or unfocused",
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
    
    # Iterate each question and get the rated answer fron user
    for i in range(0, len(questions)):
        print("")
        # This line is Equivalent to `printf("%d. %s", i + 1, questions[i])` in C language
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
