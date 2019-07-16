cha = float(input("yo how much you need to change to change in dollas "))

list = []
while cha>=0.25:
	cha = cha - 0.25
	list.append(1)
	if cha>=0.25:
		continue
a = sum(list)
print(a,"quarters")
print(float(cha))

list = []
while cha>=0.1:
	cha = cha - 0.1
	list.append(1)
	if cha>=0.1:
		continue
list
b = sum(list)
print(b,"dimes")
print(float(cha))

list = []
while cha>=0.05:
	cha = cha - 0.05
	list.append(1)
	if cha>=0.05:
		continue
list
c = sum(list)
print(c,"nickels")
print(float(cha))

list = []
while cha > 0.01:
	cha = cha - 0.01
	list.append(1)

list
d = sum(list)

list = []
while cha > 0.00:
	cha = cha - 0.01
	list.append(1)

list
e = sum(list)
print(e+d,"pennies")
print(int(cha))

f = a + b + c + d + e
print("The least amount of coins needed is ", f)