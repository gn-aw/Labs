import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)
print("Тек. состояние:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:", gc.get_stats())

id_1 = id(first)
id_2 = id(second)
del first, second
k = gc.collect()
print(k)

print("add_ex ========")

gc.disable()

f_1 = []
s_1 = []

f_1.append(s_1)
s_1.append(f_1)

f_2 = []
s_2 = []

f_2.append(s_2)
s_2.append(f_2)

f_3 = []
s_3 = []

f_3.append(s_3)
s_3.append(f_3)

del f_1, s_1, f_2, s_2, f_3, s_3

k = gc.collect()

print(k)
gc.enable()

print("prac_task ========")

