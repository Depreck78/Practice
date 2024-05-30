#User input
nums = input("Input nums: ")
target = input("Inpput Target: ")

#Splits by the spaces and stores characters in a list
lst = nums.split()

tgt = int(target)
d = {}
n = 0

#Goes through the entire input from i = 0 to i = n, converts all to integers and stores in a list
for i in range(len(lst)):
    lst[i] = int(lst[i])
print("list: ", lst)

for i in range(0, len(lst)):
    d[lst[i]] = i
    z = tgt - lst[i]
    if z in d and i != d[z]:
        x = [d[z], i]
        print(x)
    elif z not in d:
        n += 1
        if n == len(lst):
            print("None")

