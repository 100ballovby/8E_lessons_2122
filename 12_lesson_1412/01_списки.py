# вывести все четные от 0 до 15 и все нечетные от 35 до 80 и записать их в разные списки
even = []
odd = []

for i in range(0, 15, 2):
    even.append(i)
    
for j in range(35, 81, 2):
    odd.append(j)

print(even)
print(odd)
