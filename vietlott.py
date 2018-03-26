# ky 00215
from collections import Counter 

def displayResult(results, totalNumbers):
    [print("{} display {} times: {:.2%}".format(key,value,value/len(totalNumbers.keys()))) for key, value in results.items()]

def getAllNumbers(data):
    temp = []
    for item in range(len(data)):
        for i in range(len(data[item])):
            temp.append(data[item][i])

    return temp

def readDataFile():
    data = []
    # Read data from file data.txt
    files = open("./data.txt", "r")
    for file in files:
        temp = []
        [temp.append(int(x)) for x in file.rstrip().split(',')]

        # save all days
        data.append(temp)

    return data

def main():
    totalData = []
    numbers = []

    # Read data from file data.txt
    totalData = readDataFile()
    numbers = getAllNumbers(totalData)

    numbers.sort()
    flatNumbers = Counter(numbers) #Counter times display of numbers

    print('\n')
    print('##### RESULTS of {} Ky #####'.format(len(totalData)))
    displayResult(flatNumbers, flatNumbers)

    # Display top 6 numbers have display more times
    print('\n')
    print('##### TOP 6 #####')
    sorted(flatNumbers.items(), key=lambda x: x[1])

    top6 = dict(flatNumbers.most_common(6))
    displayResult(top6, flatNumbers)

main()
