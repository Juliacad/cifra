file =  open('1.txt', 'r')
file.close()
file_2 = open('2.txt', 'r')
file_2.close()
x, y, r = (1, 1, 5)
ax, ay, bx, by, cx, cy = (0, 0, 1, 6, 6, 6)
a = (ax - x) ** 2 + (ay - y) ** 2
if a < r ** 2:
       print ("точка a снаружи");
if a == r ** 2:
       print ("точка a на окружности");
if a > r ** 2:
       print ("точка a внутри круга");
b = (bx - x) ** 2 + (by - y) ** 2
if b < r ** 2:
        print ("точка b снаружи");
if b == r ** 2:
        print ("точка b на окружности");
if b > r ** 2:
        print ("точка b внутри круга");
c = (cx - x) ** 2 + (cy - y) ** 2
if c < r ** 2:
        print ("точка c снаружи");
if c == r ** 2:
        print ("точка c на окружности");
if c > r ** 2:
        print ("точка c внутри круга");