# for i in range(1,5,1):
#     for j in range(0,i,1):
#         print("*",end=" ")
#     print()
# output
# * 
# * *
# * * *
# * * * *

#<---------------------------> 

# for i in range(0,5,1):
#     for j in range(0,i,1):
#         print(i,end=" ")
#     print()
# output
# 1
# 2 2
# 3 3 3
# 4 4 4 4

#<--------------------------->

# for i in range(1,5,1):
#     for j in range(0,i,1):
#         print(j+1,end=" ")
#     print()
# output
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
        
#<---------------------------->

# for i in range(5,0,-1):
#     for j in range(0,i,1):
#         print("*",end=" ")
#     print()
# output
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

#<---------------------------->
# for i in range(1, 5 + 1):
#     print(" " * (5 - i), end=" ")
#     print("*" * (2 * i - 1))
# output
#      *
#     ***
#    *****
#   *******
#  *********

#<------------------------------>
n=int(input("Number "));
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end=" ")
#     print()
# for i in range(n):
#     for j in range(n-i-1):
#         print("* ",end=" ")
#     print()
#output
# *  
# *  *  
# *  *  *  
# *  *  *  *  
# *  *  *  *  *  
# *  *  *  *  
# *  *  *  
# *  *  
# * 