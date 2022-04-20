def find_evenodd(num):
    '''
    This function check even or odd check and return true or false respectively.
    '''
    if (num % 2 == 0):
        return True
    else:
        return False


num = int(input("Enter a number to check Even or Odd: "))


answer = find_evenodd(num)

if answer == True:
    print("even number")
else:
    print("odd")
