
def larger_value(*numbers):
    greater = 0
    for value in numbers:
        if value >= greater:
            greater = value
    return greater      

print(larger_value(5, 7, 76, 12, 56, 34))            



def smaller_value(*numbers):
    lesser = 0
    for value in numbers:
        if value <= lesser:
            lesser = value
    return lesser      

print(smaller_value(51, -7, 76, 12, 56, 34, -0.1)) 



# def math_value(x, y):
#     a = 3*x + 7*y
#     b = 3*x + 17*y - a
#     c = 4*x + 27*y - 4*a + 5*b
#     d = 8*x + 17*y + 12*a + 9*b - 4*c
#     e = 12*x + 37*y + 45*a - 13*c + 6*d
#     return a, b, c , d, e
#     alphabets = [a,b,c,d,e]

#     for values in range(*alphabets):
#         if value >= greatest:
#             greatest = value
#     return greatest 

# print(math_value(2,10))    
# print("the greatest value is ", greatest)




def factorial(x):
    
    value = 1
    for iter in range(x):
        
        value *= iter + 1
        
    return value

print (factorial(4))
