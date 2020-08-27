def divide(x, y):

    if y == 0:
        print("Error!! we cant divide by 0")
        exit(1)

    # save sign
    sign = 1
    if x * y < 0:
        sign = -1

    # convert to positive
    x = abs(x)
    y = abs(y)

    quotient = 0

    # loop while  x  >   y
    while x >= y:
        x = x - y
        quotient = quotient + 1	

    print("le reste ==", x)
    if x == 0 : 
        return True
    else: 
        return False 


if __name__ == '__main__':
    dividend = int(input("Please Enter a number to be devided by 3 : "))
    #dividend = 55
    divisor = 3
    res =  divide(dividend, divisor)
    if res == True: 
        print("divisible par 3")
    else:
        print("non divisible par 3")
    

