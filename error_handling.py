"""
#Using Else block
a={1:2,4:5,8:9}
try:
    print(a[1])
except:
    print("Error Handling")
# else:
#     print("It's Working")
#Else will work when the try block is working (If try block has no error)
#-----------------------------------------------------------------------------------
#Using Finally block
a={1:2,4:5,8:9}
try:
    print(a[1])
except:
    print("Error Handling")
finally:
    print("All Working")
#No matter the eror is present or not final block will work 
# with try block also (if ther is no error),it will work with except(If try block have error)
#
#Combination of 4 blocks Try,except,else, finally
a={1:2,4:5,8:9}
try:
    print(a[1])
except:
    print("Error Handling")
else:
    print("It's Working")

finally:
    print("All Working")
#If there is error in the try block then the 
#except block will run with except block final block will run

#Nested Exception Handling
a=10
b=5
try:
    print(a/b)
    try:
        print(a/2)
    except NameError:
        print("Name error Handling")

    else:
        print("second one")

    finally:
        print("finally block is working")
except:
    print("error Handling")

else:
    print("stage one done")

finally:
    print("its done")

"""
'''
#To create UserDefinedError
class Metro(BaseException):
    ...
def demo(x):
    if x<0:
        print("It's Working")
    else:
        raise Metro
demo(2)
----------------------------------------------------------------
class LengthError(BaseException):
    ...

def demo(a):
    if len(a)<=5:
        print("Below length")
    else:
        raise LengthError
demo("HIHELLO")
#If you want to display tour own use syntax(class Metro(BaseException))
#Otherwise it will show inbuilt error
#----------------------------------------------------------------
#Using Try and Except block
class MetroError(BaseException):
    ...
def demo(x):
    if x<0:
        print("It's Working")
    else:
        raise MetroError
try: 
    demo(20)
except:
    print("MetroError Handled")
'''
