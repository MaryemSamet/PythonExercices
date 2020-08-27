
def convert(lowerString):
    upperString = ''

    for i in range(len(lowerString)):
        if(lowerString[i] >= 'a' and lowerString[i] <= 'z'):
            upperString = upperString + chr((ord(lowerString[i]) - 32))
        else:
            upperString = upperString + lowerString[i]
            
    return(upperString)
     
    
    
    
if __name__ == '__main__':

    
    lowerString = input("Please Enter a String : ")

    res = convert(lowerString)

    print("\nOriginal String  =  ", lowerString)
    print("Result : String in Uppercase =  ", res)

