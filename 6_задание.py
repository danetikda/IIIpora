#6 задание Егэ по информатике


#Повтори 16 [Налево 36 Вперёд 4 Налево 36]
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом. 
# Точки на линии следует учитывать.

from turtle import *
tracer(0)

left(90)
for i in range(16):
    left(36)
    forward(4*40)
    left(36)

penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*40, y*40)
        dot(4, 'red')







#Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует две команды: Вперёд n (где п - целое число), вызывающая передвижение Черепахи на n единиц в том направлении, куда указывает её голова, и Направо m (где m - целое число), вызывающая изменение направления движения на m градусов по часовой стрелке. Запись
# Повтори k Команда1 Команда2 … Команда S]
# означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
# Повтори 12 |Вперёд 6 Направо 120]
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.



from turtle import *

tracer(0)
left(90)
k = 30
for _ in range(12):
    forward(6*k)
    right(120)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(5)

done()



#Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен.
#  При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует две команды: Вперёд n (где п - целое число), вызывающая передвижение Черепахи на п единиц в том направлении, куда указывает её голова, и Направо т (где т - целое число), вызывающая изменение направления движения на т градусов по часовой стрелке. Запись Повтори k [Команда1 Команда2 … Команда.S] означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
# Повтори 4 [Вперёд 9 Направо 90 Вперёд 7 Направо 90].
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.

from turtle import *

tracer(0)
left(90) #голова направлена вдоль положительного направления оси ординат
k = 30 #маштаб
for _ in range(4): #Тут менять
    forward(9*k)
    right(90)
    forward(7*k)
    right(90)

pu() #всегда писать
for x in range(-50,50): #всегда писать чтобы были точки
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(5)

done()



#Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует две команды: Вперёд n (где n - целое число), вызывающая передвижение Черепахи на n единиц в том направлении, куда указывает её голова, и Направо m (где m- целое число), вызывающая изменение направления движения на т градусов по часовой стрелке. Запись Повтори k [Команда1 Команда2 …
# КомандаS] означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
# Повтори 15 [Вперёд 3 Паправо 40]
# Определите, сколько точек с целочисленными положительными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.

from turtle import *

tracer(0)
left(90) #голова направлена вдоль положительного направления оси ординат
k = 30 #маштаб
dot(10) #начало точка (0,0)
for _ in range(15): #Тут менять
    forward(3*k)
    right(40)

pu() #всегда писать, поднимает хвост
for x in range(-50,50): #всегда писать чтобы были точки
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(5)

done()


#Исполнитель Черепаха передвигается по плоскости и оставляет след в виде линии. Черепаха может выполнять две команды: Вперёд п (п - число) и Направо т (т - число). По команде Вперёд Черепаха перемещается вперёд на п единиц. По команде Направо т Черепаха поворачивается на месте на т градусов по часовой стрелке, при этом соответственно меняется направление дальнейшего движения.
# В начальный момент Черепаха находится в начале координат и направлена вверх (вдоль положительного направления оси ординат).
# Запись Повтори k [Команда1 Команда2 … КомандаS] означает, что заданная последовательность из S команд повторится к раз.
# Черепаха выполнила следующую программу:
# Повтори 4 [Вперёд 14 Направо 90]
# Повтори 5 [Вперёд 5 Направо 45].
# Определите, сколько различных точек с целочисленными координатами будет находиться на линиях, полученных при выполнении данной программы.


from turtle import *

tracer(0)
left(90) #голова направлена вдоль положительного направления оси ординат
k = 30 #маштаб
dot(10) #начало точка (0,0)
for _ in range(4): #Тут менять
    forward(14*k)
    right(90)
for i in range(5):
    forward(5*k)
    right(45)

pu() #всегда писать, поднимает хвост
for x in range(-50,50): #всегда писать чтобы были точки
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(2)

done()



#Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует 6 команд: Поднять хвост, означающая переход к перемещению без рисования; Опустить хвост, означающая переход в режим рисования; Вперёд n (где п - целое число), вызывающая передвижение Черепахи на п единиц в том направлении, куда указывает её голова; Назад (где п - целое число), вызывающая передвижение в противоположном голове направлении; Направо m (где m - целое число), вызывающая изменение направления движения на градусов по часовой стрелке, Налево m (где m - целое число), вызывающая изменение направления движения на m градусов против часовой стрелки.
# Запись
# Повтори k [Команда1 Команда2 … КомандаS] означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
# Повтори 2 [Вперёд 10 Направо 90 Вперёд 20 Направо 90]
# Поднять хвост
# Назад 15 Направо 90 Назад 10 Налево 90
# Опустить хвост
# Повтори 2 [Вперёд 20 Направо 90 Вперёд 40 Направо 90]
# Определите, сколько точек с целочисленными координатами будут находиться внутри пересечения фигур, ограниченных заданными алгоритмом линиями, не включая точки на границах этого пересечения.

from turtle import *

tracer(0)
left(90) #голова направлена вдоль положительного направления оси ординат
k = 30 #маштаб
dot(10) #начало точка (0,0)
screensize(5000, 5000) #размер
for _ in range(2): #Тут менять
    forward(11*k)
    right(90)
    forward(20 * k)
    right(90)
pu() #опустить
back(15*k)
right(90)
back(10 *k)
left(90)
pd() #поднять хвост
for i in range(2):
    forward(20*k)
    right(90)
    forward(40 * k)
    right(90)

pu() #всегда писать, поднимает хвост
for x in range(-50,50): #всегда писать чтобы были точки
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(5)

done()



#Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует 6 команд: Поднять хвост, означающая переход к перемещению без рисования; Опустить хвост, означающая переход в режим рисования; Вперёд n (где n - целое число), вызывающая передвижение Черепахи на п единиц в том направлении, куда указывает её голова; Назад n (где п - целое число), вызывающая передвижение в противоположном голове направлении; Направо m (где m целое число), вызывающая изменение направления движения на m градусов по часовой стрелке, Налево m (где m - целое число), вызывающая изменение направления движения на т градусов против часовой стрелки. Запись
# Повтори k [Командаl Команда2 … КомандаS]
# означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
# Повтори 2 [Вперёд 10 Направо 90 Вперёд 20 Направо 90]
# Поднять хвост
# Назад 15 Направо 90 Назад 10 Налево 90
# Опустить хвост
# Повтори 2 [Вперёд 20 Направо 90 Вперёд 25 Направо 90]
# Определите, сколько точек с целочисленными координатами будут находиться внутри пересечения фигур, ограниченных заданными алгоритмом линиями, 
# включая точки на границах этого пересечения.

from turtle import *

tracer(0)
left(90) #голова направлена вдоль положительного направления оси ординат
k = 30 #маштаб
dot(10) #начало точка (0,0)
screensize(5000, 5000) #размер
for _ in range(2): #Тут менять
    forward(11*k)
    right(90)
    forward(20 * k)
    right(90)
pu() #опустить
back(15*k)
right(90)
back(10 *k)
left(90)
pd() #поднять хвост
for i in range(2):
    forward(20*k)
    right(90)
    forward(25 * k)
    right(90)

pu() #всегда писать, поднимает хвост
for x in range(-50,50): #всегда писать чтобы были точки
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(5)

done()



#Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует 6 команд: Поднять хвост, означающая переход к перемещению без рисования; Опустить хвост, означающая переход в режим рисования; Вперёд n (где п - целое число), вызывающая передвижение Черепахи на п единиц в том направлении, куда указывает её голова; Назад n (где n - целое число), вызывающая передвижение в противоположном голове направлении; Направо m (где m- целое число), вызывающая изменение направления движения на т градусов по часовой стрелке, Налево m (где m - целое число), вызывающая изменение направления движения на m градусов против часовой стрелки. Запись
# Повтори k [Команда1 Команда2 … КомандаS] означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
# Повтори 2 [Вперёд 4 Направо 90 Вперёд 7 Направо 90]
# Поднять хвост
# Вперёд 2 Направо 90 Назад 4 Налево 90
# Опустить хвост
# Повтори 2 [Вперёд 5 Направо 90 Вперёд 9 Направо 90]
# Выполняя этот алгоритм, Черепаха рисует одну за другой две фигуры. Определите, сколько точек с целочисленными координатами будут находиться внутри первой нарисованной фигуры, но не внутри второй. 
# Точки на границах указанной области учитывать не следует.

from turtle import *

tracer(1)
left(90) #голова направлена вдоль положительного направления оси ординат
k = 30 #маштаб
dot(10) #начало точка (0,0)
screensize(5000, 5000) #размер
for _ in range(2): #Тут менять
    forward(4*k)
    right(90)
    forward(7 * k)
    right(90)
pu() #поднять
forward(2*k)
right(90)
back(4 *k)
left(90)
pd() #опустить хвост
for i in range(2):
    forward(5*k)
    right(90)
    forward(9 * k)
    right(90)

pu() #всегда писать, поднимает хвост
for x in range(-50,50): #всегда писать чтобы были точки
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(5)

done()



# #(Е. Джобс) Исполнитель Чертёжник перемещается на координатной плоскости, оставляя след в виде линии. Чертёжник может выполнять команду Сместиться на (a,b) (где а, b - целые числа), перемещающую Чертёжника из точки с координатами (х, у) в точку с координатами (х+а, у+b). Если числа а, b положительные, то значение соответствующей координаты увеличивается, если отрицательные - уменьшается. Например, если Чертёжник находится в точке с координатами (4, 2), то команда Сместиться на (2,-3) переместит Чертёжника в точку (6,-1). Запись Повтори k [Команда1 Команда2 … КомандаS] означает, что последовательность из S команд повторится k раз. Чертёжнику был дан для исполнения следующий алгоритм:
# Повтори 10 [
# Сместиться на (6, 15)
# Сместиться на (-5, -5)
# Сместиться в (2, 2)
# Сместиться на (-1, -10) |
# Определите количество точек с целочисленными координатами, лежащих на линии, нарисованной Чертёжником
from turtle import *

tracer(0)
k = 30
screensize(3000, 3000)

for _ in range(10):
    goto(xcor()+6 *k, ycor()+15 *k) # текущее положение +3 +6
    goto(xcor() - 5 * k, ycor() -5 * k)
    goto(2 *k, 2*k) #относительно текущего положения в 2
    goto(xcor() - 1* k, ycor() + -10 * k)



pu() #всегда писать, поднимает хвост
for x in range(-50,50): #всегда писать чтобы были точки
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(5)

done()






###########################################################
from turtle import *

tracer(0)
k = 30
screensize(3000, 3000)

for _ in range(3):
    goto(xcor() + 3 * k, ycor() +2 * k)
    goto(xcor() - 2* k, ycor() + 3 * k)
    goto(xcor() - 3 * k, ycor() + -2 * k)
    goto(xcor() +2 * k, ycor() + -3 * k)

pu() #всегда писать, поднимает хвост
for x in range(-50,50): #всегда писать чтобы были точки
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(5)

done()

# Формула пика, прямоугольнк с целочисленными верщинами
# B = количество целочисленных точек внутри
# Г = количество целых точек на границе
# S = В + Г/2 -1

