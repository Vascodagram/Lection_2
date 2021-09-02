def number(generator):
	def decorator(*args):
		res = generator(*args)
		res_f = filter(lambda x: x % 2 == 0, res)
		return res_f
	return decorator

@number
def fibonacci(n):
	a = 0
	b = 1 
	for _ in range(n):
		a, b = b, a + b
		yield b


def main():
	print(list(fibonacci(50)))


if __name__ == "__main__":
	main()