from art import logo

#CALCULATOR FUNCTIONS

# ADD 
def add(n1, n2):
  return n1 + n2
# SUBSTRACT
def substract(n1, n2):
  return n1 - n2
# MULTIPLY
def multiply(n1, n2):
  return n1 * n2
# DIVIDE
def division(n1, n2):
  return n1 / n2

#DICTIONARY
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": division
}


def calculator():
  print(logo)
  num1 = float(input("First number: "))
  
  want_to_exit = False
  while not want_to_exit:
    print("This are the operations you can do: ")
    for key in operations:
      print(key)
    operation_symbol = input("Write only the symbol of the operation you want to make: ")
    
    num2 = float(input("Next number: "))
    
    calculation = operations[operation_symbol]
    
    answer = calculation(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    print("\n")
    choose = input("'y' to continue or 'n' to start a new calculation: ")
  
    if choose == 'y':
      num1 = answer
    else:
      want_to_exit = True
      calculator()
  
calculator()