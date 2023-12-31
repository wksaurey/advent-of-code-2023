with open('input/day4.text') as file:
    games = file.read().splitlines()

gameCounts = [1] * len(games)

for gameIndex, game in enumerate(games):
    print(gameCounts)
    game = game.split(':')[1].strip().split('|')
    winningNums = list(map(int, game[0].split()))
    nums = list(map(int, game[1].split()))

    gamescore = 0
    for num in nums:
        if num in winningNums:
            gamescore += 1
    print(f'Game {gameIndex}: {gamescore}')
    for tempGameIndex in range(gameIndex+1, gameIndex + gamescore + 1):
        if tempGameIndex >= len(games):
            break
        if tempGameIndex == 5:
            print('Something is wrong...')
        gameCounts[tempGameIndex] += gameCounts[gameIndex]
        
gameCountSum = 0
for index, gameCount in enumerate(gameCounts):
    print(f'Game {index+1} Count: {gameCount}')
    gameCountSum += gameCount


print(f'\nTotal Count: {gameCountSum}')