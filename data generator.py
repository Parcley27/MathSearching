import csv
import random
import time

steps = 0
trialCount = 1000

sizeVariations = 100
listSize = 1000000
        
# Clear file to write new data
with open("time data.csv", "w", newline = "") as file:
    writer = csv.writer(file)

    writer.writerow(["Search Size", "Search Steps (avg)", "Search Time (avg)"])

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

for size in range(sizeVariations):
    steps = 0

    listSize = 1000000 * (size + 1)
    list = [i * 2 for i in range(listSize)]

    print(f"Starting {trialCount} tests for {listSize} item lists...")

    start = time.time()

    for trial in range(trialCount):
        target = list[random.randint(0, len(list) - 1)]

        targetIndex = search(list, target, 0, len(list) - 1)

    end = time.time()
    length = end - start

    averageSteps = steps / trialCount
    averageTime = length / trialCount

    print(f"{trialCount} tests for {listSize} item lists have finished.")
    print(f"Avg. Steps: {averageSteps}, Avg. Time: {averageTime}s, Total Time: {length}s")


    with open("time data.csv", "a", newline = "") as file:
        writer = csv.writer(file)

        writer.writerow([listSize, averageSteps, averageTime])

    print("Data saved.")