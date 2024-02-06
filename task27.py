input_str = ("She sells sea shells on the sea shore "
             "The shells that she sells are sea shells "
             "I'm sure.So if she sells sea shells on the sea shore "
             "I'm sure that the shells are sea shore shells")
print(input_str)
input_str = input_str.replace('.' ,' ')
print(input_str)
input_lst = input_str.split()
print(input_lst)
for i in range(len(input_lst)):
    input_lst[i] = input_lst[i].lower()
print(input_lst)
print(len(set(input_lst)))
print('*' * 15)
res = len(set(i.lower() for i in input_str.replace('.' ,' ').split()))
print(res)