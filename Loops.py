# n=10
# i=1
# while(i<=10):
#     print(i)
#     i+=1

#<---------------------------->

# for i in range(10):
#     print(i)

#<---------------------------->

# for i in range(10):
#     print(i,end='@')

#<---------------------------->

# fruits=["Apple","Mango","Banana"]
# for i in fruits:
#     print(i)

#<---------------------------->

# fruits={"1":"Apple","2":"Mango","3":"Banana"}
# for i in fruits:
#     print(i,fruits[i])


#<----------------------------->

# fruits="applebananaorange"
# for i in fruits:
#     print(i,end="")
#     if i=='e':
#           break

#<----------------------------->

# fruits="applebananaorange"
# for i in fruits:
#     print(i,end="")
#     if i=='a':
#           continue

#<----------------------------->

# fruits = {
#     'a' : "apple",
#     'b' : "banana",
#     'c' : "orange"
# }
# for key, value in fruits.items():
#     if value == "banana":
#         print("Kela detected!")
#         break
#     print(key, value)

#<------------------------------>
# num=int(input("Enter the number: "))
# i=1
# while i<=10:
#     print(i,"x",num,"=",num*i)
#     i+=1

#<------------------------------->

# num=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(num):
#     print(num[i],end=" ")
#     i+=1

#<-------------------------------->

# num=[1,4,9,16,25,36,49,64,81,100]
# t=int(input("Enter the search element: "))
# i=0
# while i<len(num):
#     if(num[i]==t):
#         print("Element found at",i),
#     i+=1

# <-------------------------------->

# num=[1,2,3,4,5]
# for i in num:
#     print(i)

# <--------------------------------->

# range()
# num=range(5)
# for i in num:
#     print(i,end=" ")

# <---------------------------------->

# pass
# for i in range(5):
#     pass
# print("Navneet")

# <----------------------------------->

# n=int(input("Enter the number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("Total sum:-",sum)

# <----------------------------------->

n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("TFactorial:-",fact)

