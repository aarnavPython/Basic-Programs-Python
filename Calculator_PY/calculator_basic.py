# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y
   

def calculate():
 print("Select operation:")
 print("Add")
 print("Subtract")
 print("Multiply")
 print("Divide")
 # Take input from the user 
 choice = int(input("Enter choice (1/2/3/4):"))

 num1 = int(input("Enter first number: "))
 num2 = int(input("Enter second number: "))

 if choice == 1 :
   print(num1,"+",num2,"=", add(num1,num2))

 elif choice == 2 :
   print(num1,"-",num2,"=", subtract(num1,num2))

 elif choice == 3 :
   print(num1,"X",num2,"=", multiply(num1,num2))

 elif choice == 4 :
  print(num1,"÷",num2,"=", divide(num1,num2))
 else:
   print("Invalid input")

   

def recalculate():
  recalc = input("Do you want to calculate again? Y for Yes and N for No.")

  if recalc == "Y": 
    calculate()

  if recalc == "y":
    calculate()

  if recalc == "N":
    print ("Thanks for using this simple calculator!")

  if recalc == "n":
    print ("Thanks for using this simple calculator!")
    
    
calculate()
recalculate()




  
#This is basic code. You should use this as reference as a beginner.
  
