import time as measureTime

test = False
time = []
distance = []
if test:
    time =     71530
    distance = 940200
else:
    time =     50748685
    distance = 242101716911252

def main():
    starttime = measureTime.time()
    possibleWins = []
    possibleRace = 0
    for buttonTime in range(time):
        if getDistance(buttonTime, time) > distance:
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