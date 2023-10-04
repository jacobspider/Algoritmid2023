from functools import lru_cache

@lru_cache(maxsize= 1000)
def fibonacci(n):
	if n < 0:
		print("Fibonacci arvud ei ole miinuses")
	if n ==1:
		return 1
	elif n== 2:
		return 1
	elif n> 2:
		return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
	n = 5
	print(n, "th Fibonacci Number: ")
	print(fibonacci(n))


