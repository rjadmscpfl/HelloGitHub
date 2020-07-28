### elif 

#num1 = int(input("첫번째 정수 입력 >> "))
#num2 = int(input("두번째 정수 입력 >> "))
#
#if num1 > num2:
#    print("First number is bigger")
#elif num1 < num2:
#    print("Second number is bigger")
#elif num1 == num2:
#    print("Both numbers are same")


score = int(input("점수 입력 >> "))

if score<=100 and score>=90: # 90<=score<=100:
    result = "A"
elif score<=90 and score>=80:
    result = "B"
elif score<=90 and score>=80:
    result = "C"
elif score<=90 and score>=80:
    result = "D"
else:
    result = "F"

print("{} is {}.".format(score, result))
