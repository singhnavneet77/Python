# for i in range(1,5,1):
#     for j in range(0,i,1):
#         print("*",end=" ")
#     print()

#<---------------------------> 

# for i in range(0,5,1):
#     for j in range(0,i,1):
#         print(i,end=" ")
#     print()

#<--------------------------->

# for i in range(1,5,1):
#     for j in range(0,i,1):
#         print(j+1,end=" ")
#     print()
        
#<---------------------------->

# for i in range(5,0,-1):
#     for j in range(0,i,1):
#         print("*",end=" ")
#     print()

#<---------------------------->
for i in range(1, 5 + 1):
    print(" " * (5 - i), end=" ")
    print("*" * (2 * i - 1))
