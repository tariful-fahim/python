def hello_func():
   print("Hello Bangladesh")

hello_func()

def return_func():
    return "good Morning"

print(return_func())

#parameter pass

def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(20))

#What *args allows you to do is take in more 
# arguments than the number of formal arguments that you previously defined.

#**kwargs in function definitions in python is used to pass a keyworded, variable-length argument list

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

#student_info('CSE','Math','Art', 'physics' name='kodu',age='22')
course = ['Math', 'physics','English']
info = {'name':'kodu','age':22}
student_info(*course,**info)
