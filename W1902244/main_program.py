# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1902244
# Date: 4/18/2022



from horizontal_Histogram import hori_Histogram
from vertical_Histogram import vertical_Histogram
from print_list import list_Output
from list_write import file_Write
from file_Output import file_Output

input_Loop = True
final_Loop = True
progress_Count = 0
trailer_Count = 0
retriever_Count = 0
excluded_Count = 0
outcome_Total = 0

count_List = []
output_List =[]

count  = 0

list_Append = []
var_Name = ""

def list_Add(Name,Pass,Defer,Fail):
    global list_Append
    output_List.append(Name)
    output_List.append(Pass)
    output_List.append(Defer)
    output_List.append(Fail)


def is_Valid(input):
    """Checking the validity of the input
       Input -  Credits at pass, defer and fail
       Output - Validity of the input
    """
    try:
        int(input)
        input = int(input)
        if input in range(0,121,20):
            return True
        else:
            print("OUT OF RANGE")
            return False
    except ValueError:
        print("INTEGER REQUIRED")
        return False
    
def total_Correct(credits_Pass,credits_Defer,credits_Fail):
    """Checking if the total is correct or not
       Input  - credits at pass, defer and fail
       Output - Validity of the input
    """
    global total
    global progress_Count
    global trailer_Count
    global retriever_Count
    global excluded_Count
    total = int(credits_Pass) + int(credits_Defer) + int(credits_Fail)
    if total > 120 or total < 120:
        print("Total incorrect")
    else:
        credits_Pass = int(credits_Pass)
        credits_Defer = int(credits_Defer)
        credits_Fail = int(credits_Fail)
        
        if(credits_Pass == 120):
            print("Progress")
            progress_Count += 1
            name = "Progress-"
            list_Add(name,credits_Pass,credits_Defer,credits_Fail)

        elif(credits_Pass + credits_Defer <= 40 and credits_Fail >= 80):
            print("Exclude")
            excluded_Count += 1
            name = "Exclude-"
            list_Add(name,credits_Pass,credits_Defer,credits_Fail)
            
        elif(credits_Pass <= 80 and credits_Defer + credits_Fail <= 120):
            print("Module retriever")
            retriever_Count += 1
            name = "Module retriever-"
            list_Add(name,credits_Pass,credits_Defer,credits_Fail)
            
        elif(credits_Pass == 100 and (credits_Defer == 20 or credits_Fail == 20)):
            print("Progress(module trailer)")
            trailer_Count += 1
            name = "Module retriever-"
            list_Add(name,credits_Pass,credits_Defer,credits_Fail)
            
    count_List.append(progress_Count)
    count_List.append(retriever_Count)
    count_List.append(trailer_Count)
    count_List.append(excluded_Count)

            
    return progress_Count,retriever_Count,trailer_Count,excluded_Count,output_List
def main():
    global input_Loop 
    global progress_Count
    global trailer_Count
    global retriever_Count
    global excluded_Count 
    global outcome_Total

    global count_List
    global output_List

    global count
    while input_Loop:
        credits_Pass = input("Enter your total PASS credits: ")
        if (is_Valid(credits_Pass)):
             
            credits_Defer = input("Enter your total DEFER: ")
            if(is_Valid(credits_Defer)):
                
                credits_Fail = input("Enter your total FAIL: ")
                if(is_Valid(credits_Fail)):
                    
                    if(total_Correct(credits_Pass,credits_Defer,credits_Fail)):
                        outcome_Total += 1
                        print("\n")
                        user_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
                        if(user_input == "y"):
                            continue
                        elif(user_input == "q"):
                            input_Loop = False
                        else:
                            choice = False
                            while choice is False:
                                print("invalid text input.")
                                user_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
                                if user_input == "y":
                                    choice =  True
                                else:
                                    choice = False
def choice():                                    
    print("\n")
    global final_Loop
    while final_Loop:
        print("""
To print data as a Horizontal Histogram enter - H
To print the data as a Vertical histogram enter - V
To print data as a List enter - L
To write data into to text file enter - T
        """)


        user_Choice = input("Enter you choice:-")
        user_Choice = user_Choice.upper()
        
        if user_Choice == "H":
            hori_Histogram(progress_Count,retriever_Count,trailer_Count,excluded_Count,outcome_Total)
        elif user_Choice == "V":
            vertical_Histogram(progress_Count,trailer_Count,retriever_Count,excluded_Count,count_List,outcome_Total)
        elif user_Choice == "L":
            list_Output(output_List)
        elif user_Choice == "T":
            file_Write(output_List)
            print("\n")
            print("""
Do you want to print the data written to the text file on to the console
If Yes enter - Y
If Not enter - N""")
            choice = input("Enter your Choice:-")
            choice = choice.upper()
            if choice == "Y":
                file_Output()
            elif choice == "N":
                break
            else:
                print("Invalid input")
                choice = input("Enter your Choice:-")
                choice = choice.upper()
        
        print("Do you want to get the output in a different method \nIf Yes enter Y \nIf you want to end the program enter Q")
        choice = input("Enter your Choice:-")
        choice = choice.upper()
        last_Loop = True
        while last_Loop:
            if choice == "Y":
                final_Loop = True
                last_Loop = False
            elif choice == "Q":
                last_Loop = False
                final_Loop = False
            else:
                print("Invalid input")
                choice = input("Enter your Choice:-")
                choice = choice.upper()
                final_Loop = True
                last_Loop = True
    
            
    print("Program Terminated")


mode_Loop = True    
while mode_Loop:
    print("To select the student mode enter - 1 \nTo select the staff mode enter - 2")
    mode = input("Enter the mode you want to use-")
    if mode == "1" or mode == "2":
        break
    else:
        mode_Loop = True

if mode == "1":
    main()
elif mode == "2":
    main()
    choice()
    
    
        
    
    
