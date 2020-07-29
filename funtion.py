# def f(X):
#   exe
#   return Y

## delete "w" in sentence
#def string_replace(list_test):
#    for review in list_test:
#        print(review.replace("w",""))

def number_minus(a, b):
    return a - b 

def s_replace(str_test):
    return str_test.replace("w","")

#total = number_sum(10, 20)
#print(total)

#a1 = int(input("first number >> "))
#b1 = int(input("Second number >> "))
#result = number_minus(a1, b1)
#print(result)

#comment = input ("input comment >> ")
#result = s_replace(comment)
#print(result)

#def cal(A, B, C):
#    """
#    This is for you
#    """
#    if C == "+":
#        result = A + B
#    elif C == "-":
#        result = A - B
#    return result
#
#A = int(input("first nmuber >> "))
#B = int(input("second number >> "))
#C = input("(+, -) >> ")
#result = cal(A, B, C)
#print(result)

def add_sum(*args):
    sum = 0
    for num in args:
        sum = sum + num
    return(sum)

result = add_sum(1, 2, 3, 10, 20, 30)
print(result)




