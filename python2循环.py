'''if语句'''
x = int(input("Enter a number: "))
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
'''while循环'''
i = 0
while i < 5:
    i+=1
    print(i)
'''for循环'''
for j in range(0,5,1):#(起始, 结束, 步长)
    print(j)
s = 'Hello, World!'
for i in s:
    print(i)
'''break'''#终止整个程序
for i in range(10):
    if i == 5:
        break
    print(i)
'''continue'''#终止某一步，继续程序
for i in range(10):
    if i == 5:
        continue
    print(i)