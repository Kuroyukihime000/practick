primer = input( "Введите выражение которое хотите посчитать => " )
for i in primer:
    if i == ' ':
       primer = primer[primer.index(i)] + primer[primer.index(i) + 1]
operations = ['+', '-', '*','/','^']
prior_operations = ['/','*','^']
 
def add(a, b):
    return a + b
    
def subtrack(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b


