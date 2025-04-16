#Вопрос 1. Укажите такое значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть своим первым ходом.
#Вопрос 2. Найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия,
#  причём Петя не может выиграть за один ход, но может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
#Найденные значения запишите в ответе в порядке возрастания.
#Вопрос 3. Найдите минимальное значение S, при котором Ваня может выиграть первым или вторым ходом при любой игре Пети,
#  но у него нет стратегии, которая позволит ему гарантированно выиграть первым ходом. Если найдено несколько значений S, в ответе запишите минимальное из них.

#Одна куча. +1 *2. Петя не выйграл за 1 ход. Ваня выиграл первый ходом. p -Текущий ход игры. Нечётный ход - Петя, чётный Ваня.
def f(x,p):
    if x >=129 or p>2: #В начальный момент в куче 1<=S<=128
        return p == 2
    if p % 2: #Ход нечётный - Петя
        return f(x+1,p+1) or f(x*2,p+1)
    else:
        return f(x+1,p+1) and f(x*2,p+1) #Ваня
    

print('Задание 19:', [s for s in range (1,129) if f(s,0)])

def f(x,p):
    if x >=129 or p>3:
        return p == 3
    if p % 2==0: 
        return f(x+1,p+1) or f(x*2,p+1)
    else:
        return f(x+1,p+1) and f(x*2,p+1)
    

print('Задание 20:', [s for s in range (1,129) if f(s,0)])

def f(x,p):
    if x >=129 or p>4:
        return p == 2 or p ==4
    if p % 2: 
        return f(x+1,p+1) or f(x*2,p+1)
    else:
        return f(x+1,p+1) and f(x*2,p+1)
    

print('Задание 21:', [s for s in range (1,129) if f(s,0)])



#Одна куча. -2, -5, //3. p -Текущий ход игры. Нечётный ход - Петя, чётный Ваня.

def f(x, p):
    if x <= 19 or p > 2:  # В начальный момент в куче 1<=S<=128
        return p == 2
    if p % 2:  # Ход нечётный - Петя
        return f(x - 2, p + 1) or f(x - 5, p + 1) or f(x // 3, p+1)
    else:
        return f(x - 2, p + 1) and f(x - 5, p + 1) and f(x //3, p+1) # Ваня


print('Задание 19:', [s for s in range(100, 19, -1) if f(s, 0)])


def f(x, p):
    if x <= 19 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x - 2, p + 1) or f(x - 5, p + 1) or f(x // 3, p+1)
    else:
        return f(x - 2, p + 1) and f(x - 5, p + 1) and f(x // 3, p+1)


print('Задание 20:', [s for s in range(100,19,-1) if f(s, 0)])


def f(x, p):
    if x <= 19 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f(x - 2, p + 1) or f(x - 5, p + 1) or f(x // 3, p+1)
    else:
        return f(x - 2, p + 1) and f(x - 5, p + 1) and f(x // 3, p+1)


print('Задание 21:', [s for s in range(1, 129) if f(s, 0)])



#Если есть доп условие о том что ход не должен повторяться
def f(x, p, k):
    if x >=76 or p>2:
        return p ==2
    if k==0:
        if p %2:
            return f(x +1, p+1, 1)or f(x+3, p +1, 2) or f(x*3, p+1,3)
        else:
            return f(x + 1, p + 1, 1) and f(x + 3, p + 1, 2) and f(x * 3, p + 1, 3)
    elif k==1:
        if p %2:
            return f(x+3, p +1, 2) or f(x*3, p+1,3)
        else:
            return f(x + 3, p + 1, 2) and f(x * 3, p + 1, 3)
    elif k==2:
        if p %2:
            return f(x +1, p+1, 1)or f(x*3, p+1,3)
        else:
            return f(x + 1, p + 1, 1) and f(x * 3, p + 1, 3)
    elif k==3:
        if p %2:
            return f(x +1, p+1, 1)or f(x+3, p +1, 2)
        else:
            return f(x + 1, p + 1, 1) and f(x + 3, p + 1, 2)

print("Задание 19:", [s for s in range(1,76)if f(s,0,0)])

def f(x, p, k):
    if x >=76 or p>3:
        return p ==3
    if k==0:
        if p %2==0:
            return f(x +1, p+1, 1)or f(x+3, p +1, 2) or f(x*3, p+1,3)
        else:
            return f(x + 1, p + 1, 1) and f(x + 3, p + 1, 2) and f(x * 3, p + 1, 3)
    elif k==1:
        if p %2==0:
            return f(x+3, p +1, 2) or f(x*3, p+1,3)
        else:
            return f(x + 3, p + 1, 2) and f(x * 3, p + 1, 3)
    elif k==2:
        if p %2==0:
            return f(x +1, p+1, 1)or f(x*3, p+1,3)
        else:
            return f(x + 1, p + 1, 1) and f(x * 3, p + 1, 3)
    elif k==3:
        if p %2==0:
            return f(x +1, p+1, 1)or f(x+3, p +1, 2)
        else:
            return f(x + 1, p + 1, 1) and f(x + 3, p + 1, 2)

print("Задание 20:", [s for s in range(1,76)if f(s,0,0)])

def f(x, p, k):
    if x >=76 or p>4:
        return p ==2 or p==4
    if k==0:
        if p %2:
            return f(x +1, p+1, 1)or f(x+3, p +1, 2) or f(x*3, p+1,3)
        else:
            return f(x + 1, p + 1, 1) and f(x + 3, p + 1, 2) and f(x * 3, p + 1, 3)
    elif k==1:
        if p %2:
            return f(x+3, p +1, 2) or f(x*3, p+1,3)
        else:
            return f(x + 3, p + 1, 2) and f(x * 3, p + 1, 3)
    elif k==2:
        if p %2:
            return f(x +1, p+1, 1)or f(x*3, p+1,3)
        else:
            return f(x + 1, p + 1, 1) and f(x * 3, p + 1, 3)
    elif k==3:
        if p %2:
            return f(x +1, p+1, 1)or f(x+3, p +1, 2)
        else:
            return f(x + 1, p + 1, 1) and f(x + 3, p + 1, 2)

print("Задание 21:", [s for s in range(1,76)if f(s,0,0)])




    