import random
number = random.randint(-10000, 10000)
number = str(number)
print(number)
new_number= number[-1]
print(new_number)
new_number = int(new_number)
print ("Last digit of {} is {}".format(number, new_number))
if new_number > 5:
  print("and is greater than 5")
elif new_number == 0:
  print("and is 0")
elif new_number < 6 and new_number != 0:
  print("and is less than 6 and not 0")
