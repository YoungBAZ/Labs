# Question 1
# limit = eval(input("Input a number: "))
# for i in range(0,limit+1):
#   if i % 2 == 0:
#     print(i)

# Question 2
# limit = eval(input("Input a number: "))
# sum = 0
# for i in range(0,limit+1):
#   if i % 2 != 0:
#     sum += i
# print(sum)

# Question 3
# limit = eval(input("Input a number: "))
# for i in range(1,limit+1):
#   if i == 11:
#     break
#   else:
#     pass
#   print(f"{i} * {limit} = {i*limit}")

# Question 4
# sum = 0
# count = 0
# while True:
#   num = eval(input("Enter numbers to add (-1 to stop): "))
#   if num == -1:
#     break
#   else:
#     count += 1
#     sum += num
# print(
#   f"The sum of the numbers is {sum}\nThe count of the numbers is {count}\nThe average of the numbers is {sum/count}"
# )

# Question 5
# numbers = []
# while True:
#   num = eval(input("Enter numbers to add (-1 to stop): "))
#   if num <= -1:
#     break
#   else:
#     numbers.append(num)
#     numbers.sort()
#     print(len(numbers), f"The maximum number is {numbers[(len(numbers) - 1)]}, and the minimum number is {numbers[0]}")

# Question 6
# sum = 0
# while True:
#   num = eval(input("Enter numbers to add (-1 to stop): "))
#   if num == -1:
#     print(f"The sum of the odd numbers is {sum}.")
#     break
#   elif num % 2 == 0:
#     continue
#   else:
#     sum += num
#     continue

# Question 7
# num1 = eval(input("Enter a number: "))
# num2 = eval(input("Enter a number: "))
# sum = 0
# count = 0
# for i in range(min(num1,num2),max(num1,num2)+1):
#   if i % 2 == 0:
#     count += 1
#     sum += i
# print(sum)

# Question 8
# sum = 0
# for i in range(0,101):
#   if i % 5 == 0 or i % 3 == 0:
#     pass
#   else:
#     sum += i
# print(sum)

# Question 9
# results = []
# while len(results) < 10:
#   num = eval(input("Enter a number: "))
#   if num == 1:
#     result = "pass"
#   else:
#     result = "fail"
#   results.append(result)
#   continue
# print(results)

# Question 10
# number = 2000
# for i in range (2016, 2020 + 1):
#   increase = (number*0.03)
#   number += increase
#   print(f"The number in {i} is {round(number,3)}")
