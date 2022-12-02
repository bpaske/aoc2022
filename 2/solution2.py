played_scores = {'X':0, 'Y':3, 'Z':6}
rock_played = {'A Y', 'B X', 'C Z'}
paper_played = {'A Z', 'B Y', 'C X'}
siscors_played = {'A X', 'B Z', 'C Y'}

score = 0
with open('./input.txt') as f:
    for line in f:
        sl = line.strip()
        if sl in rock_played:
            score += 1
        elif sl in paper_played:
            score += 2
        elif sl in siscors_played:
            score += 3 
        last_char = sl[-1]
        score += played_scores[last_char]

print(score)