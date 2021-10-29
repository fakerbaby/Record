
list1=[1,3,2,4]
list2=[42,231,5,4]

data = zip(list1, list2)
data = sorted(data)
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1) 
print(list2)