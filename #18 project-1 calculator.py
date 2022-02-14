# 1) TAKE TWO INPUT BOTH WILL BE NUMBERS
# 2) ASK USER WHAT OPERATION TO DO
# 3) RETURN THE RESULT

# TAKING INPUT
num1 = float(input("Enter The First Number:- "))
num2 = float(input("Enter The Second Number:- "))

# ASKING FROM USER WHAT TO DO 
options = '1) ADDITION \n2) SUBTRACT \n3) MULTIPLY\n4) DIVIDE\n'
print(options)
userInp = input("Enter Option Here:- ")

if userInp == '1':
    print(f"ADDITION OF {num1} and {num2} IS {num1 + num2}")
elif userInp == '2':
     print(f"SUBTRACTTION OF {num1} and {num2} IS {num1 - num2}")
elif userInp == '3':
     print(f"MULTIPLICATION OF {num1} and {num2} IS {num1 * num2}")
elif userInp == '4':
     print(f"DIVIDATION OF {num1} and {num2} IS {num1 / num2}")
else:
    print("NO INPUT")


