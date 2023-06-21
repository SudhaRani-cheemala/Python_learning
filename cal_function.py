def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations={
"+":add,
"-":sub,
"*":mul,
"/":div
}
num1=int(input("Enter first number?:"))
for symbol in operations:
    print(symbol)
operation_symbol=input("pick an operation from the line above:")
num2=int(input("Enter second number?:"))
calculate_function=operations[operation_symbol]
answer=calculate_function(num1,num2)
print(f"{num1} {operation_symbol} {num2}={answer}")

