#У исполнителя Калькулятор две команды, которым присвоены номера:
# 1. прибавь 2
# 2. умножь на 3
# Сколько есть программ, которые число 1 преобразуют в число 55?

def f(x,y):
    if x>y: return 0
    if x==y:return 1
    return f(x+2,y)+f(x*3,y)

print(f(1,55))


def f(x,y):
    if x>y: return 0
    if x==y:return 1
    return f(x+1,y)+f(x+4,y)+f(x+5,y)

print(f(30, 46))


#Условие прибавь предыдущее
def f(x,y):
    if x>y: return 0
    if x==y:return 1
    return f(x+2,y)+f(x+3,y)+f(x*2-1,y)

print(f(2, 11))

# сделай чётное и нечётное

def f(x,y):
    if x>y: return 0
    if x==y:return 1
    return f(x+1,y)+f(x*2,y)+f(2*x+1,y) +f(x*10,y)

print(f(1, 15))


#условие припиши 1
def f(x,y):
    if x>y: return 0
    if x==y:return 1
    return f(x+1,y)+f(int('1'+str(x)),y)

print(f(1, 512))


# Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Прибавить 2
# 3. Прибавить 4
# Программа для исполнителя Калькулятор - это последовательность команд.
# Сколько существует программ, для которых при исходном числе 2
# результатом является число 13, и при этом траектория вычислений не содержит число 6?

def f(x,y):
    if x>y or x == 6: return 0
    if x==y:return 1
    return f(x+1,y) + f(x+2,y) +f(x+4,y)

print(f(2,13))


#условие не содержит цифру 5

def f(x,y):
    if '5' in str(x): return 0
    if x>y:return 0
    if x==y:return 1
    return f(x+1,y)+f(x+3,y)+f(x*3,y)

print(f(1,49))


#условие содержит число 10

def f(x,y):
    if x>y:return 0
    if x==y:return 1
    return f(x+1,y)+f(x*2,y)

print(f(1,10)*f(10,21))


# У исполнителя имеются три команды, которые обозначены латинскими буквами:
# A. Вычесть 1
# B. Вычесть 2
# C. Найти целую часть от деления на 3
# Первая команда уменьшает число на 1, вторая - уменьшает его на 2, третья - находит целую часть от деления числа на 3. Программа для исполнителя- это последовательность команд.
# Сколько существует программ, для которых при исходном числе 16 результатом является число 6, при этом траектория вычислений содержит число 11?

def f(x,y):
    if x<y:return 0 #если уменьшаем знак нужно поменять > на <
    if x==y:return 1
    return f(x-1,y)+f(x-2,y)+f(x//3,y)

print(f(16,11)*f(11,6))


#условие содержит 6 и 10

def f(x,y):
    if x>y:return 0
    if x==y:return 1
    return f(x+1,y)+f(x+3,y)+f(x*2,y)

print(f(2,6)*f(6,10)*f(10,14))


#условия содержит 15 35 не содержит 20 25

def f(x,y):
    if x>y or x in (20,25):return 0
    if x==y:return 1
    return f(x+1,y)+f(x+2,y)+f(x*3,y)

print(f(15,35)*f(35,25))



#Условие предпоследняя команда являеться 1. Прибавить 1
#Исходное 5, результат 32
def f(x,y):
    if x>y:return 0
    if x==y:return 1
    return f(x+1,y)+f(x*2,y)


print(f(5,30)+f(5,15))
#30+1+1=32
#(15+1)*2=32


# 1. Прибавить 1
# 2. Прибавить 4
# 3. Умножить на 2
# Программа для исполнителя Калькулятор - это последовательность команд.
# Сколько существует программ, состоящих из 7 команд, для которых при исходном числе 3 результатом является число 27?

def f(x,k):
    if x ==27 and k ==7:
        return 1
    if x>27: return 0
    return f(x+1,k+1)+f(x+4,k+1)+f(x*2,k+1)

print(f(3,0))

# 1. Вычесть 1
# 2. Обнулить
# Первая команда уменьшает число на 1. Вторая команда обнуляет все ненулевые разряды, кроме старшего (например, для исходного числа 11101 результатом работы команды будет число 10000), если таких разрядов нет, то данная команда не выполняется.
# Сколько существует программ, которые исходное двоичное число 1100 преобразуют в двоичное число 100?


def f(x,y):
    if x<y:return 0
    if x==y:return 1
    if bin(x).count('1')==1:return f(x-1,y)
    else:
        return f(x-1,y)+f(int('1'+bin(x)[3:].replace('1','0'),2),y)

print(f(int('1100',2), int('100',2)))

# 1. Прибавь 1
# 2. Прибавь 3
# 3. Умножь на 2
# Первая команда увеличивает число на экране на 1, вторая увеличивает его на 3, третья - умножает на 2. Программа для исполнителя - это последовательность команд.
#  Сколько существует программ, которые преобразуют исходное число 3 в число 30 и при этом не содержат двух команд «Прибавить 1» подряд?

def f(x,y,k):
    if x>y:return 0
    if x==y:return 1
    if k ==0:
        return f(x+1,y,1)+f(x+3,y,0)+f(x*2,y,0)
    else:
        return f(x+3,y,0)+f(x*2,y,0)

print(f(3,30,0))

# 1. прибавь 1
# 2. прибавь 3
# 3. умножь на 2
# 4. умножь на 3
# Выполняя первую из них, исполнитель увеличивает число на экране на 1, выполняя вторую - увеличивает на 3, выполняя третью - умножает на 2, выполняя четвертую - умножает на 3. 
# Сколько существует различных программ, преобразующих число 1 в число 9999 и не содержат двух подряд идущих команд сложения и двух подряд идущих команд умножения?

def f(x,y,k):
    if x>y:return 0
    if x==y:return 1
    cont = 0
    if k !=1:
        cont += f(x+1,y,1)+f(x+3,y,1)
    if k !=2:
        cont += f(x*2,y,2)+f(x*3,y,2)
    return cont
print(f(1,9999,0))


# 1. Прибавь 1
# 2. Умножь на 3
# 3. Умножь на 4
# Первая команда увеличивает число на экране на 1, вторая умножает его на 3, третья - умножает на 4.
#  Сколько существует различных программ, которые преобразуют исходное число 3 в число 300 и содержат не более пяти команд умножения?

def f(x,y,k):
    if x>y:return 0
    if x==y:return 1
    if k<5:
        return f(x+1,y,k)+f(x*3,y,k+1)+f(x*4,y,k+1)
    else:
        return f(x+1,y,k)


print(f(3,300,0))


# Исполнитель преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавь 1
# 2. Умножь на 2
# 3. Умножь на 5
# Первая команда увеличивает число на экране на 1, вторая умножает его на 2, третья - умножает на 5.
#  Сколько существует различных программ, которые преобразуют исходное число 3 в число 260 и содержат больше команд умножения, чем сложения?

def f(x,y,raz):
    if x >y :return 0
    if x==y:return 1 if raz>0 else 0
    return f(x+1, y, raz-1)+f(x*2,y,raz+1)+f(x*5,y,raz+1)

print(f(3,260,0))


# 1. Прибавь 1
# 2. Прибавь 3
# 3. Умножь на 2
# Первая команда увеличивает число на экране на 1, вторая увеличивает его на
# 3, третья - умножает на 2. Программа для исполнителя - это последовательность команд.
#  Сколько существует программ, которые преобразуют исходное число 3 в число 60, и при этом траектория вычислений содержит число 20 и не содержит чисел 30 и 40. 
# Также программа не должна содержать двух команд «Умножь на 2» подряд.


from functools import lru_cache

@lru_cache
def f(x,y,k):
    if x>y:return 0
    if x==y:return 1
    if x==30 or x==40: return 0
    count = f(x +1, y,0)
    count += f(x+3,y,0) if x not in (18,19) else 0
    count += f(x*2,y,1) if k!=1 and not(11<=x<=19) else 0
    return count

print(f(3,60,0))


# A. Вычесть 1
# B. Прибавить 2
# C. Умножить на 3
# Найдите количество существующих программ, для которых при исходном числе 5 результатом является число 62,
#  и при этом траектория вычислений содержит число 32 и не содержит чисел, оканчивающихся на 0,
#  а программа не содержит двух команд вычитания подряд.

from functools import lru_cache


@lru_cache
def f(x, y, k, h32):
    if x > y + 1 or x % 10 == 0: return 0
    if x == y: return h32
    if x == 32: h32 = True
    if k == 1:
        return f(x + 2, y, 2, h32) + f(x * 3, y, 3, h32)
    else:
        return f(x - 1, y, 1, h32) + f(x + 2, y, 2, h32) + f(x * 3, y, 3, h32)


print(f(5, 62, 0, 0))

# 1. Прибавь 3
# 2. Умножь на 2 и прибавь 1
# Сколько различных результатов можно получить из исходного числа 2 после выполнения программы, содержащей ровно 13 команд?

s = set()
def f(x,k):
    if k ==13:
        s.add(x)
    else:
        f(x+3,k+1)
        f(2*x+1,k+1)

f(2,0)
print(len(s))

####
s = set()
def f(x,k):
    if k ==8:
        s.add(x)
    else:
        f(x+1,k+1)
        f(x+5,k+1)
        f(x*3, k+1)

f(1,0)
print(len(s&set(range(1000,1025)))) #& берём пересечение и там и там & -это 




   












