with open('input/day4.text') as file:
    games = file.read().splitlines()

totalScore = 0
for gameIndex, game in enumerate(games):
    game = game.split(':')[1].strip().split('|')
    winningNums = list(map(int, game[0].split()))
    nums = list(map(int, game[1].split()))

    gamescore = 0
    for num in nums:
        if num in winningNums:
            if gamescore == 0:
                gamescore = 1
            else:
                gamescore = gamescore * 2
    totalScore += gamescore
    print(f'Game {gameIndex}: {gamescore}')

print(f'\nTotal Score: {totalScore}')