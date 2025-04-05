# Use first line for steps, second for time

with open("time data.txt", "w") as file:
    csvFile = open("step data.csv", "r")
    #csvFile = open("timeData.csv")

    csvData = csvFile.readlines()
    csvArray = csvData[0].split(", ")

    for entry in csvData:
        entry = entry.split(",")
        
        file.writelines([f"{entry[0]}   {entry[1]}\n"])
        #file.writelines([f"{entry[0]}	{entry[2]}"])