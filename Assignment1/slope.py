n = int(input("How many numbers are we adding up bro? "))

print("Aight bet")

list = []

for i in (range(n)):
	s = int(input("gimme a number: "))
	list.append(s)
print(sum(list))