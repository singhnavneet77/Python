import numpy as np
a=np.zeros((3,4))
# print(a)

b=np.linspace(10,30,5)
# print(b)

c=np.arange(10,30,5)
# print(c)

d=np.random.randint(10,30,(3,4))
e=np.random.randint(20,50,(3,4))
print(d)
print("\n")
print(e)
print("\n")
# concat two np array

print(np.add(d,e))
print("\n")
print(np.multiply(d,e))
print("\n")
print(np.subtract(d,e))
print("\n")
# similar * /  - +

