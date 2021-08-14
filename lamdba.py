# מה זה lambda?
# זו בעצם הדרך שלי לשים פונקציה או קטע קוד בתוך משתנה.
# כדאי לי לעשות זאת בגלל שאפשר לשלוף אותו במהירות ולא צריך לכתוב אותו כל פעם, רק את המשתנה.
#labda
code_execute_print_with_hello = lambda: print('hello world')
code_execute_print_with_hello()


def my_filters(x):
    return True             #return > 8 ====> output: [9]

l1 = [1,2,3,4,5,6,7,8,9]
print(list(filter(my_filters, l1)))
                                                               #the function "even" and  the 'print' in row 21 is the same
def even(x):                                                   #but 'even is a function and the print is doing with lambda.

    return  x % 2 == 0

l2 = range(100)
print(list(filter( even, l2)))
print('===================================')
print((list(filter(lambda x: x % 2 == 0, l2))))
print(list(filter(lambda x: x % 2 != 0, l1)))
print(list(filter(lambda x: x %7 ==0, l1)))
print(list(filter(lambda x: x > 50, l1)))
print('==================================')



l1 = range(9)
def power2(x):
    return  x * x
#1*1=1, 2*2=4 3*3=9 4*4=16...
print(list(map(power2, l1)))