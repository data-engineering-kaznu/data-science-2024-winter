print("This is calculator")

def adding(a, b):
    return a + b

def substracting(a, b):
    return a - b

def multiplacation(a, b):
    return a * b

def division(a, b):
    return a / b

def exponentiation(a, b):
    return a ** b
        

def main():
    a = int(input("Input first operand: "))
    b = int(input("Input second operand: "))
    
    #Adding
    result_of_adding = adding(a, b)
    print(result_of_adding)

    #Substacting
    result_of_substracting = substracting(a, b)
    print(result_of_substracting)
    
    #Multiplication
    result_of_multiplication = multiplacation(a, b)
    print(result_of_multiplication)
    
    #Division
    result_of_division = division(a, b)
    print(result_of_division)

    #Exponentiation
    result_of_exponentiation = exponentiation(a, b)
    print(result_of_exponentiation)

    #print(substracting(adding(adding(adding(adding(5,4), multiplacation(3, exponentiation(3, 2)), division(exponentiation(3, 3), exponentiation(3,2)))), exponentiation(10,2), 8))
    return 0

if __name__ == "__main__":
    main()