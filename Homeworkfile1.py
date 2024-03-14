import os

# 163
# names_list = []
# mylist = os.listdir('BabyNames')
# for i in mylist:
#     with open(f'BabyNames/{i}', 'r') as file:
#         name = file.readline()
#     name = name.split(' ')
#     names_list.append(name[0])
# print(set(names_list))


# 164
# mylist = os.listdir('BabyNames')
# year = input('Enter year: ')

# for i in mylist:
#     if i[:4] == year and 'Boys' in i:
#         with open(f'BabyNames/{i}', 'r') as file:
#             boys = file.readlines()
#     elif i[:4] == year and 'Girls' in i:
#         with open(f'BabyNames/{i}', 'r') as file1:
#             girls = file1.readlines()
            
# girls_list = []
# boys_list = []
# for i in girls:
#     girls_list.append(i.split()[0])
# for i in boys:
#     boys_list.append(i.split()[0])
    
# print(set(girls_list).intersection(set(boys_list)))


# 166
# mylist = os.listdir('BabyNames')

# for i in mylist:
#     with open(f'BabyNames/{i}', 'r') as file:
#         if 'Boys' in i:
#             boys = file.readlines()
#         elif 'Girls' in i:
#             girls = file.readlines()
            
# girls_list = []
# boys_list = []
# for i in girls:
#     girls_list.append(i.split()[0])
# for i in boys:
#     boys_list.append(i.split()[0])
    
# print(set(boys_list))
# print(set(girls_list))