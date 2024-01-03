import time as measureTime

test = False
time = []
distance = []
if test:
    time =     [7, 15, 30]
    distance = [9, 40, 200]
else:
    time =     [50,  74,   86,   85]
    distance = [242, 1017, 1691, 1252]

def main():
    starttime = measureTime.time()
    possibleWins = []
    for index, raceTime in enumerate(time):
        record = distance[index]
        print(raceTime)
        print(record)
        possibleRace = 0
        for buttonTime in range(raceTime):
            if getDistance(buttonTime, raceTime) > record:
                possibleRace += 1
        possibleWins.append(possibleRace)

    score = calculateScore(possibleWins)
    print(f'Score: {score}')
    endtime = measureTime.time()
    print(f'Run in {endtime-starttime} seconds')

def calculateScore(possibleWins):
    score = 1
    for possibleRaces in possibleWins:
        score = score * possibleRaces
    return score



def getDistance(buttonTime, raceTime):
    return buttonTime * (raceTime - buttonTime)

main()