ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
DRAW = 3
WIN = 6

outcome = {
    (ROCK, PAPER): LOSE,
    (ROCK, ROCK): DRAW,
    (ROCK, SCISSORS): WIN,
    (PAPER, SCISSORS): LOSE,
    (PAPER, PAPER): DRAW,
    (PAPER, ROCK): WIN,
    (SCISSORS, ROCK): LOSE,
    (SCISSORS, SCISSORS): DRAW,
    (SCISSORS, PAPER): WIN,
}

opponent_map = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

my_map = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

lines = [line.strip().split(" ") for line in open('02_input', 'r').readlines()]

rounds = [(my_map[s[1]], opponent_map[s[0]]) for s in lines]
print(sum([r[0] + outcome[r] for r in rounds]))

outcome_map = {
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}

score = 0
for line in lines:
    opponent_play = opponent_map[line[0]]
    desired_outcome = outcome_map[line[1]]
    for play, outcome_score in outcome.items():
        if outcome_score == desired_outcome and play[1] == opponent_play:
            score += (play[0] + outcome_score)
            break
print(score)
