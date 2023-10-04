my_list = ['ammu', 'shaanu', 'chiu']
my_list.append('nandu')
my_list.insert(1, 'amma')

for t in my_list:
    print(t)
print("--------------------------")

my_list.pop()
print(my_list)
print("--------------------------")
my_list1 = ['papa', 'achan']
new_list = my_list + my_list1
print(new_list)
print("--------------------------")
my_new_list = my_list1 * 2
print(my_new_list)
print("--------------------------------------------------------------")

random_list = [1,4,2,6,0,758,5683,789]
random_list.sort()
print(random_list)
print("--------------------------------------------------------------")

my_list.sort(reverse=True)
print(my_list)
print("--------------------------------------------------------------")



original_list = [1,2,3,2,8,6,2,4]
assigned_list = original_list.copy()
original_list.append(9)
print(original_list)
print(assigned_list)
print(3 in original_list)
counting_2 = original_list.count(2)
print(counting_2)
print(sum(original_list))
print(min(original_list))
print(max(original_list))
