user_input = input( "Введите выражение которое хотите посчитать => " )

def add(a, b):
    return a + b
    
def subtrack(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

if "+" in user_input:
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
