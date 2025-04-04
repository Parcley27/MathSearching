import random

listMax = 10000

print("Writing list")

list = [i * 2 for i in range(listMax)]

print("Searching a list of numbers:")

firstTen = ""

for i in range(10):
    firstTen += f"{list[i]} " if i < len(list) else ""

print(f"{firstTen.strip()} ... {list[-1]}")

target = list[random.randint(0, len(list) - 1)]

print("\nTarget:")
print(target)
print("")

steps = 0

def search(list, target, min, max):
    global steps
    steps += 1

    middleIndex = min + (max - min) // 2

    if min > max:
        return -1 

    if list[middleIndex] == target:
        return middleIndex
    
    elif list[middleIndex] < target:
        return search(list, target, middleIndex + 1, max)
    
    elif list[middleIndex] > target:
        return search(list, target, min, middleIndex - 1)

targetIndex = search(list, target, 0, len(list) - 1)

if targetIndex != -1:
    print(f"The index of {target} is: {targetIndex}")
    print(f"(list[targetIndex] = {list[targetIndex]}, target = {target})")
    print(f"The target was found in {steps} steps.")

else:
    print("The target was not found in the list.")
    