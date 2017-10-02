import time
# These are all our little functions

def add(x,y):
  return x+y

def subtract(x,y):
  return x-y
  
def multiply(x,y):
  return x*y
  
def divide(x,y):
  return x/y 
  
def calculate():
  print ("Welcome to Calculator+")
  time.sleep(2)
  print ("\n")
  print ("Choose your operation:")
  print ('1-Add')
  print ('2-Subtract')
  print ('3-Multiply')
  print ('4-Divide')
  print ('\n')
  choice =  int(input("Select operation (1/2/3/4): "))
  
  print ('\n')
  
  num_1 =  int(input("Enter your first number: "))
  num_2 = int(input("Enter your second number: "))
  
  if choice == 1:
    print (num_1,"+",num_2, "=", add(num_1,num_2))
  elif choice == 2:
    print (num_1,"-",num_2, "=", subtract(num_1,num_2))
  elif choice == 3:
    print (num_1,"*",num_2, "=", multiply(num_1,num_2))
  elif choice == 4:
    print (num_1,"/",num_2, "=", divide(num_1,num_2))
  else:
    print ("Invalid Input.")
    
def recalculate():
  recalc_Choice = input("Do you want to calculate again? Y for yes and N for no (case sensitive.")
  
  if recalc_Choice == "Y":
    time.sleep(2)
    calculate()
  else:
    print ("Thank you for using this Calculator! Have a nice day!")
    
calculate()
recalculate()
  

  
