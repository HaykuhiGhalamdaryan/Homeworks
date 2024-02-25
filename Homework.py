# 173
# def summ():
#     n = input('Enter number: ')
#     if n == '':
#         return 0
#     else:
#         return summ() + int(n)
    
# print(summ())

# 174
# def greatest_common_divisor(a,b):
#     if b == 0:
#         return a
#     c = a % b
#     return greatest_common_divisor(b,c)

# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
# print(greatest_common_divisor(a,b))

# 184
# def flatten_list(arr):
#     if arr == []:
#         return []
#     elif type(arr[0]) == list:
#         return flatten_list(arr[0]) + flatten_list(arr[1:])
#     return [arr[0]] + flatten_list(arr[1:])
# arr = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
# print(flatten_list(arr))