
'''This code written below is by me which is a bit difficult to understand, 
therefore I also added instructor's program for future references'''

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
    
def inp(t):
    print('''
    +
    - 
    *
    /
    ''')
    op = input("Pick an operation from the above: ")
    b = float(input("What's the next number?: "))
    answer = operation(t,b,op)
    return answer
def string(t1,t2,oper,aner):
    ma = f"{t1} " + oper + f" {t2}" + " = " + str(aner)
    print(ma)
    
    
def operation(x,y,opr):
    if opr == "+":
        ans = add(x,y)
    elif opr == "-":
        ans = sub(x,y)
    elif opr == "*":
        ans = multi(x,y)
    else:
        ans = div(x,y)
    string(x,y,opr,ans)
    return ans

def start(t3):
    fa = inp(t3)
    return fa 
def start_over():
    a = float(input("What's the first number?: "))
    lol = start(a)
    return lol 

print(logo)
z = start_over()
print(f"So the answer is {z}")
conti = True
while conti == True:
    res = input(f"Type 'y' to continue calculating with {z}, or type 'n' to start a new calculation, or 's' to stop the calculator")
    if res == "y":
        z = start(z)
        print(z)
    elif res == "n":
        start_over()
    else:
        conti = False
    



""" Instructors's code --- 
from replit import clear


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()

"""



