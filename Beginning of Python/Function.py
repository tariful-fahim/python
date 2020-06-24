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


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

#student_info('CSE','Math','Art', 'physics' name='kodu',age='22')
course = ['Math', 'physics','English']
info = {'name':'kodu','age':22}
student_info(*course,**info)