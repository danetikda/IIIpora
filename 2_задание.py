#Это файл со всеми типами решений задачь ЕГЭ по информатике
# 2 задание Егэ по иноформатике
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x == (w or y)) or ((w <= z) and (y <= w))):
                    print(x, y, z, w)



from itertools import *

def f(x,y,z,w):
    return (x or y or z)<= (x and (y or w)) #Сюда писать выражение


for s in product([0,1], repeat=4): #repeat зависит от пропущенных значений, счёт не забываем с нуля. 
    table = [(1,0, s[0], 0),
             (s[1],1,1,s[2]),
             (1,1,s[3],1)] #Сюда переписывать таблицу
    if len(table)== len(set(table)):
        for n in permutations("xyzw"):
            if [f(**dict(zip(n,line)))for line in table] == [0,0,0]: #тут менять значения функции F
                print(n)
