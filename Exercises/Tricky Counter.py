# #counter
# my_list = [1,2,3,4,5,6,7,8,9,10] #sum up the total of the list using looping
# print(sum(my_list))
#
# counter = 0
#
# for num in my_list:
#     counter = counter + num
#
# print(counter)


my_list = list(range(1,25))
print(my_list)
sum_total = 0
for num in my_list:
    sum_total = sum_total + num
print(sum_total)
print(sum(my_list))