file =  open('3.txt', 'r')
n = file.read()
file.close()
n = [1,10,2,9]
num = list(n)
f = round(sum(num)/len(num))
a = (abs(f - num[0])) + (abs(f - num[1])) + (abs(f - num[2])) + (abs(f - num[3]))
print(a)