# Text Files:-.txt,.docx,.log
# Binary Files:-.mp4,.mov,.png,.jpeg
# f=open("demo.txt","r")
# data=f.read()
# print(data)

# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)
# f.close()


# Data over write
# f=open("demo.txt","w")

# f.write("I want to learn AIML")
# f.close()

# f=open("demo.txt","a")

# f.write(" and App devlopment")
# f.close()

# Over writing form starting use r+
# f=open("demo.txt","r+")
# f.write("You are learning")
# f.close()

filename = "demo.txt"  # Replace with your actual file name

with open(filename) as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}: {line.strip()}")