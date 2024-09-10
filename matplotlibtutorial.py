import matplotlib.pyplot  as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
z = np.cos(x)
# print(x)
# print(y)
# print(z)

# <------------------------------->
# This will show sine graph
# plt.plot(x,y)
# plt.show()

# <------------------------------->
# This will show cosine graph
# plt.plot(x,z)
# plt.show()

# <------------------------------->
# Adding title x-axis & y-axis labels
# plt.plot(x,z)
# plt.xlabel('angle')
# plt.ylabel('sine value')
# plt.title('sine wave')
# plt.show()

# <------------------------------->
# Parabola
x = np.linspace(-10,10,20)
y = x**2
# plt.plot(x,y)
# plt.show()

# plt.plot(x,y,'r+')
# plt.show()

# plt.plot(x,y,'g.')
# plt.show()

# x = np.linspace(-5,5,20)
# plt.plot(x,np.sin(x),'g-')
# plt.plot(x,np.cos(x),'r--')
# plt.show()

# <------------------------------->
# Bar graph
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# languages = ["English","Hindi","French","German","Spanish"]
# people = [20,12,30,45,15]
# ax.bar(languages,people)
# plt.xlabel('LANGUAGES')
# plt.ylabel('PEOPLE')
# plt.show()

# <------------------------------->
# Pie Chart
# fig1 = plt.figure()
# ax = fig1.add_axes([0,0,1,1])
# languages = ["English","Hindi","French","German","Spanish"]
# people = [20,12,30,45,15]
# ax.pie(people, labels=languages, autopct= '%1.1f%%')
# plt.show()

# <------------------------------->
# Scatter plot
# x = np.linspace(0,10,30)
# y = np.sin(x)
# z = np.cos(x)
# fig2 = plt.figure()
# ax = fig2.add_axes([0,0,1,1])
# ax.scatter(x,y,color = 'g')
# ax.scatter(x,z,color = 'b')
# plt.show()

# <------------------------------->
# 3d Scatter plot
fig3 = plt.figure()
ax = plt.axes(projection='3d')
z = 20*np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x,y,z,c=z,cmap='Blues')
plt.show()