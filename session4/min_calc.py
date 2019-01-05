nums = [1, 2, 5, -14, -99, 241]
print(nums)

# print(min(list))
# print(list.index(min(list)))

min_num = 9999999
for index, x in enumerate(nums):
    if x < min_num:
        min_num = x
        min_index = index
print(min_num)
print(min_index)