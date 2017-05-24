def get_even_numbers(number):
	if number < 0 : return
	even = [x for x in range(number+1) if x % 2 == 0]
	return even

n = eval(input("enter a number:"))
Result = get_even_numbers(n)
print(Result)
