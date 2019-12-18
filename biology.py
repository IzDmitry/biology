import time  # тут библиотека времени
import itertools # генерит ОЧЕНЬ много вариантов
import re #  регулярочки для поиска 

start = time.clock()
num = input("Типы гамет =  ") # сюда пишем типы гамет
t = int(len(num) / 2)

x = sorted(set(list(itertools.combinations(num, t))))
x = ["".join(i) for i in x]
x = str(x)
print("Типы гамет = ", num, "\n")
if t == 2:
	p = re.compile(r"[Aa][Bb]")
	m = p.findall(x)
elif t == 3:
	p = re.compile(r"[Aa][Bb][Cc]")
	m = p.findall(x)
elif t == 4:
	p = re.compile(r"[Aa][Bb][Cc][Dd]")
	m = p.findall(x)
elif t == 5:
	p = re.compile(r"[Aa][Bb][Cc][Dd][Ee]")
	m = p.findall(x)
elif t == 6:
	p = re.compile(r"[Aa][Bb][Cc][Dd][Ee][Ff]")
	m = p.findall(x)
elif t == 7:
	p = re.compile(r"[Aa][Bb][Cc][Dd][Ee][Ff][Gg]")
	m = p.findall(x)
elif t == 8:
	p = re.compile(r"[Aa][Bb][Cc][Dd][Ee][Ff][Gg][Kk]")
	m = p.findall(x)	
elif t == 9:
	p = re.compile(r"[Aa][Bb][Cc][Dd][Ee][Ff][Gg][Kk][Ll]")
	m = p.findall(x)
else:
	m = "Цомк"

c = len(m)
print(m, "\n\nЧисло типов гамет = ", c, "\n")
finish = time.clock()
print("Посчитал за = ", finish - start, "сек")