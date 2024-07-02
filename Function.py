# def fun(a,b):
#     sum=a+b
#     return sum

# print(fun(2,3)) 


# def avg(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
#     return avg

# avg(1,2,3)


# list=[1,3,2,44,56,7,788,88]
# def listlen(list):
#     print(list,end=" ")
#     print()
#     print(len(list))

# listlen(list)


# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# factorial(5)

# RECURSION
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)

def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

print(fact(5))