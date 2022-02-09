import time, itertools, re 

num = input("\nТипы гамет =  ")
t = int(len(num) / 2)

start = time.time()

x = sorted(set(list(itertools.combinations(num, t))))

x = ["".join(i) for i in x]
x = str(x)
if t >= 2:
	p = re.compile(r"[a-zA-Z][a-zA-Z]", re.S)
	b = p.findall(num)
	b[:] = ["[" + id + "]"for id in b] 
	b = "".join(b)
	p = re.compile(r"" + b)
	m = p.findall(x)
else:
	m = "Неверное значение"

c = len(m)
print("\n", m, "\n\nЧисло типов гамет = ", c, "\n")
finish = time.time()
print("Посчитал за = ", finish - start, "сек")
