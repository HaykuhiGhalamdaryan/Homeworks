# 149
# try:
#     with open('myfile','r') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('File not found')

# 150
# try:
#     with open('myfile','r') as file:
#         text = file.readlines()
# except FileNotFoundError:
#     print('File not found')  
# print(text[-10:])

# 151
# def cat_files(file1,file2):
#     try:
#         with open(file2,'r') as x:
#             text = x.readlines()
#         for i in text:
#             with open(file1,'a') as y:
#                 y.write(i)
#         return 'It\'s working.'
#     except FileNotFoundError:
#         return 'File not found.'
    
# file1 = input('Enter file1: ')  
# file2 = input('Enter file2: ')  
# print(cat_files(file1,file2))   
