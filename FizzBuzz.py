# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".


for n in range(1,101):
	if n % 15 == 0:
		i = "FizzBuzz"
	elif n % 3 == 0:
		i = "Fizz"
	elif n % 5 == 0:
		i = "Buzz"
	else:
		i = n
	print(i)
  
