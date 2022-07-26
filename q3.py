def status(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")
    if age>22:
        print("eligible for mrg")
    else:
        print("not eligible for mrg try after some time")
try:
    num = int(input("Enter your age: "))
    status(num)
except ValueError:
    print("Only positive integers are allowed you ......")
finally:
    print("finally block....")
    ######################################
    '''OUTPUT:-
    Enter your age: 23
   eligible for mrg
   finally block....
    '''