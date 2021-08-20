"""
Simple Calculator + - * / %
"""

FirstInput = float(input("Input first number: "))
Operator = input("Input your operator: ")
SecondInput = float(input("Input second number: "))

if(Operator == '+'):
    print(round((FirstInput + SecondInput), 2))
elif(Operator == '-'):
    print(round((FirstInput - SecondInput), 2))
elif(Operator == '*'):
    print(round((FirstInput * SecondInput), 2))
elif(Operator == '/'):
    print(round((FirstInput / SecondInput), 2))
elif(Operator == '%'):
    print(round((FirstInput % SecondInput), 2))
else:
    print("ERROR")