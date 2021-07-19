#Tutorial 2
#Lists

nums = [25,14,15,95,34]
name = ['Praveen','Pravin','Prawin','Pravyn']
values = [25.4, 'Praveen',19,'Pravyn']
mil = [nums,values,name]

print("\nappend method in list")
print("nums ", nums)
nums.append(36)
print("nums.append(36): ",nums)

print("\nInsert method in list")
print("\nnums\n",nums)
nums.insert(2,45)
print("nums.insert(2,45): ", nums)

print("\ndelete with respect to values")
print("\nnums\n",nums)
nums.remove(45)
print("nums.remove(45): ", nums)

print("\ndelete with respect to index")
print("\nnums\n",nums)
nums.pop(1)
print("nums.pop(1): ", nums)

print("\ndelete last element")
print("\nnums\n",nums)
nums.pop()
print("nums.pop(): ", nums)

print("\ndelete range of entries")
print("\nnums\n",nums)
del nums[2:]
print("del nums[2:]: ", nums)


print("\nadd range of entries")
print("\nnums",nums)
nums.extend([29,34,45,20])
print("nums.extend([29,34,45,20]): ", nums)

print("min(nums) ",min(nums))
print("max(nums) ",max(nums))
print("sum(nums) ",sum(nums))

nums.sort()
print("nums.sort()", nums)
