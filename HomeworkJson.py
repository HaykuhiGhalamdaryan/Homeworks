# 1
import json

# data = {'key1' : "value1", "key2" : "value2"}
# jsondata = json.dumps(data)
# print(jsondata)

# 2
# data1 = json.loads(jsondata)
# print(data1['key2'])

# 3
# PrettyPrint = json.dumps(data,indent=2,separators=(',',' = '))
# print(PrettyPrint)

# 4
# data = {"id" : 1, "name" : "value2", "age" : 29}

# with open('data.json','w') as file:
#     json.dump(data,file,indent=4,sort_keys=True)

# 5
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# jsondata = json.loads(sampleJson)
# print(jsondata['company']['employee']['payble']['salary'])