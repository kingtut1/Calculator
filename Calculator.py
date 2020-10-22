def add(a,b):
    sum = a + b 
    print("Sum: ", sum)


def sub(a,b):
    sum = a - b 
    print("Difference:",sum) 


def multi(a,b):
    sum = a * b
    print("Product:",sum)

def quotient(a,b):
    sum = a / b
    print("Quotient:",sum)

def main():
    a = int(input("Please enter a number: "))
    b = int(input("Please enter another number: "))
    
    add(a,b)
    sub(a,b)  
    multi(a,b)
    quotient(a,b)

main()