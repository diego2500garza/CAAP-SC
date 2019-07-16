n = input("enter yo n ")

beg_Fibo = 0
initial_Fibo = 1

for i in range(1,n):
	c = beg_Fibo + initial_Fibo
	beg_Fibo = initial_Fibo
	initial_Fibo = c
print c