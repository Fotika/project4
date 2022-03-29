# Favour Otika
# 005159016
name = input("Enter the file name:")

f= open(name, "r")

numbers=[]

count=0

ans=0

for x in f:

    numbers.append(int(x))

    ans+=int(x)

    count+=1
    print( "Final score:",(ans-min(numbers))/(count-1))

    print("Result stored in output.txt")

    g= open("output.txt","w+")

    g.write(str((ans-min(numbers))/(count-1)))
