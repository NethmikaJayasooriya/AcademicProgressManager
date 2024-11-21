# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: .w2053761......# Date: ..2023/12/13............
print("*"*70)


#import histogram file
from w2053761_Part1_D import *

# Define the credits
credits = [0, 20, 40, 60, 80, 100, 120]

#INITIALIZING VARIABLES
Pass_mark = 0
Second_Input = 0
Third_Input = 0
count= 0
user_input=''
progress_result_list = []
result_rows_list = []

# Function to calculate the marks
def marks(Pass_mark, Second_Input, Third_Input):
  if Pass_mark == 120 and Second_Input == 0 and Third_Input == 0:
      row = ["Progress" , [Pass_mark, Second_Input, Third_Input]]
      return "Progress" , row
  if Pass_mark == 100 and Second_Input in [0, 20] and Third_Input in [0, 20]:
      row = ["Progress-module trailer" , [Pass_mark, Second_Input, Third_Input]]
      return "Progress-module trailer" , row
  if Pass_mark in [0,20,40,60,80] and Second_Input in [0, 20, 40, 60, 80, 100, 120] and Third_Input < 80:
      row = ["Do not Progress - module retriever" , [Pass_mark, Second_Input, Third_Input]]
      return "Do not Progress - module retriever" , row
  if Pass_mark in [0,20,40] and Second_Input in [0,20,40] and Third_Input >= 80:
      row = ["Exclude" , [Pass_mark, Second_Input, Third_Input]]
      return "Exclude" ,row

#main function
def main():
   print("Enter data for each student.\nstaff member can input more than one input.\n")
   #identify the user
   Valid_inputs = [1, 2]
   try:
        user_input = int(input("If you are a student Enter no:1," " " "If you are a staff Member Enter no:2:"))#Get the identity from the user
        print("\n")
        if user_input not in Valid_inputs:
            print("Invalid input")
   except ValueError:
        print("Integer required")

   count = 1
   while True:# Main loop to get user input
       print("Input range is (20,40,60,80,100,120)")
       print("\n")
       #exception handling for if user enters invalid input
       try:
           Pass_mark = int(input("Enter the pass mark : "))# Get the pass mark from the user
           if Pass_mark not in credits:
               print("Out of range")
               continue

           Second_Input = int(input("Enter your total Defer credits:"))# Get the Defer mark from the user
           if Second_Input not in credits:
               print("Out of range")
               continue

           Third_Input = int(input("Enter your total Fail credits:"))# Get the Fail mark from the user
           if Third_Input not in credits:
               print("Out of range")
               continue
          #check total credits
           Obtained_mark = Pass_mark + Second_Input + Third_Input
           if Obtained_mark != 120 :
               print("Total incorrect")
               continue

           result, row = marks(Pass_mark, Second_Input, Third_Input)
           # Keep track of each progression outcome
           progress_result_list.append(result)
           result_rows_list.append(row)
           print(result)

       except ValueError:
           print("Integer required")
           continue
       #Give results to the students and break
       if user_input==1:
             result, row = marks(Pass_mark, Second_Input, Third_Input)
             break
       elif user_input==2:
       # Ask the user if they want to enter another set of data
        print("\n")
        check_again = str(input("Would you like to enter another set of data?"+"\n"+"Enter 'y' for yes or 'q' to quit and view results:"))
        print("\n")
        if check_again.lower() == 'y':
           count = count + 1
           continue
        elif check_again.lower() == 'q': # If the user wants to quit
            graph(progress_result_list)#call the histrogram
            #create student_results Text file and save the results
            for row in result_rows_list:
                print(f"{row[0]} - {', '.join(map(str, row[1]))}")
            with open("student_results.txt", "a") as f:
                for row in result_rows_list:
                    f.write(f"{row[0]} - {', '.join(map(str, row[1]))}\n")
            with open("student_results.txt", "r") as f:
                print(f.read())
            break

        else:
           print("Invalid input")
           break
          

main()

   
