import random
number = random.randint(-10000, 10000)
number = str(number)
num = number[-1]
if int(number) < 0:
  new_number = int(num) * -1
print(new_number) 
if new_number > 5:
  print("Last digit of {} is {} and is greater than 5".format(number, new_number))
elif new_number == 0:
  print("Last digit of {} is {} and is 0".format(number, new_number))
elif new_number < 6 and new_number != 0:
  print("Last digit of {} is {} and is less than 6 and not 0".format(number, new_number))
