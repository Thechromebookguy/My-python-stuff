# Program make a simple calculator the choice of operation will

# continue until option 7 is entered and the program stops.

    
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two number
def divide(x, y):
    return x / y

# This function works out a percentage
def percentage(x, y):
    return x /100 * y

# This function works out numbers raised to a power

# In python the calculation is x**y i.e 2**3 = 8,not 2^3 = 8

def power (x, y):
    return x**y




exit = True
while exit == True:
 print('  ')
 print("Select operation.")
 print("1.Add")
 print("2.Subtra:ct")
 print("3.Multiply")
 print("4.Divide")
 print("5.Percentage")
 print("6.Power")
 print("7.Quit calculator")
 print('  ')         
 

 
# Take input from the user
 choice = input("Enter choice(1/2/3/4/5/6/7): ")

# Check if choice is one of the four options
 if choice in ('1', '2', '3', '4','5','6'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        

        if   choice == '1':
          print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
          print(num1, "-", num2, "=", subtract(num1, num2))
            
        elif choice == '3':
          print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
          print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice == '5':
          print(num1, "% of" , num2, "is", percentage(num1, num2))
            
        elif choice == '6':
          print(num1 ** num2,('is ', num1, 'raised to the power of ', num2))
        elif choice == '7':
          exit = False
   
        
 else:
       exit = False

       
