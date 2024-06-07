def fibonacciSeries(i):
	if i<=1:
		return i 
	else:
		return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))
	

num=10
for i in range(num):
	a = fibonacciSeries(i)
	print(a, end=" ")