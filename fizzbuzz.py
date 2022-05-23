# fizzbuzz - iterates the intergers from 1 to 50, for multiples of 3 print "fizz"
# for multiples of five, print "buzz"
# for numbers that are multiples of 3 and 5, print "fizzbuzz"

list = []
for x in range(0,20):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0:
        print("fizz")
    else:
        print(x)

