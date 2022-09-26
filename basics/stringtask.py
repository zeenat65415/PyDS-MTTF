# #print("\n")
# print(r"\n")#raw data or print('\\n')


# #multiline string input
# data=''
# while True:
#     line=input()# if line == '':
#     if not line:
#         break
#     data += line + '\n'
# print(data)  

print('\\n')
print(r'\n')

# multiline string input
data=''
while True:
    line = input()
    if not line:   
        break
    data += line + '\n'    
print("----->OUTPUT<-----")
print(len(data), 'chars')  