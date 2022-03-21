a=10
b=0

#indention is very much important in python
# try block contains the exception statement and except contains printing of the message
try:
    k = int(input("enter a number"))
    print(k)
    print(a/b)
    # to print actual exception here we are exception object as e
except ZeroDivisionError as e:
    print("Divide by zero exception. please check! ", e)
    #to handle the input given by user. we can specify the exact error type to handle exception
except ValueError as e:
    print("please enter integer number")
except Exception as e:
    print("unknown error ", e)
    #it doesnt matter if there is any exception or not the finally block will execute
finally:
    print ("Bye")