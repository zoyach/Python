num = int(input("Enter a number to check Even or Odd: "))


def find_evenodd(num):
    '''
    This function check even or odd check and return true or false respectively.
    '''
    if (num%2==0):
       print(num, "is an Even number")
    else:
      print(num,"is an Odd number")
     
find_evenodd(num)



