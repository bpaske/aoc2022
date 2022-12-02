played_scores = {'X':1, 'Y':2, 'Z':3}
won_games = {'A Y', 'B Z', 'C X'}
lost_games = {'A Z', 'B X', 'C Y'}
drawn_games = {'A X', 'B Y', 'C Z'}

score = 0
with open('./input.txt') as f:
    for line in f:
        sl = line.strip()
        if sl in won_games:
            score += 6
        elif sl in drawn_games:
            score += 3
        last_char = sl[-1]
        score += played_scores[last_char]

print(score)