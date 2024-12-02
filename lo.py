user_input = input( "Введите выражение которое хотите посчитать => " )

def add(a, b):
    return a + b
    
def subtrack(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

def degree(a,b):
    return a**b

def factorial(a):
    factorial = 1
    for i in range (2,a+1):
        factorial *= i
    return factorial

if "**" in user_input:
    user_input = user_input.split('**')
    for i in range(0,len(user_input)):
        user_input[i] = float(user_input[i])
    result = degree(user_input[i], user_input[i+1])
    print(result)

elif "!" in user_input:
    user_input = user_input.split('!')
    final_split = user_input[0].split(' ')
    nomber = int(final_split[-1])
    result = factorial(nomber) 
    print(result)
elif "+" in user_input:
    user_input = user_input.split('+')
    for i in range(0,len(user_input)):
        user_input[i] = float(user_input[i])
    result = add(user_input[0], user_input[1])
    print(result)
elif "*" in user_input:
    user_input = user_input.split('*')
    for i in range(0,len(user_input)):
        user_input[i] = float(user_input[i])
    result = multiply(user_input[0], user_input[1])
    print(result)
elif "-" in user_input:
    user_input = user_input.split('-')
    for i in range(0,len(user_input)):
        user_input[i] = float(user_input[i])
    result = subtrack(user_input[0], user_input[1])
    print(result)
elif "/" in user_input:
    user_input = user_input.split('/')
    for i in range(0,len(user_input)):
        user_input[i] = float(user_input[i])
    result = division(user_input[0], user_input[1])
    print(result)
else :
    print('ERROR!!!')
