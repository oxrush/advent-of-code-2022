
ROCK, PAPER, SCISSORS = 0, 1, 2
OPPONENT, PLAYER, DRAW = 0, 1, 2


def get_rounds():
    rounds = []

    with open("input.txt") as file:
        for line in (line.strip() for line in file if line.strip() != ""):
            opponent = {"A": ROCK, "B": PAPER, "C": SCISSORS}[line[0]]
            player = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}[line[2]]
            rounds.append((opponent, player))

    return rounds


def determine_winner(opponent, player):
    return {
        (ROCK, ROCK): DRAW,
        (ROCK, PAPER): PLAYER,
        (ROCK, SCISSORS): OPPONENT,
        (PAPER, ROCK): OPPONENT,
        (PAPER, PAPER): DRAW,
        (PAPER, SCISSORS): PLAYER,
        (SCISSORS, ROCK): PLAYER,
        (SCISSORS, PAPER): OPPONENT,
        (SCISSORS, SCISSORS): DRAW
    }[(opponent, player)]


def determine_score(opponent, player):
    shape_score = {ROCK: 1, PAPER: 2, SCISSORS: 3}[player]

    winner = determine_winner(opponent, player)
    win_score = {OPPONENT: 0, DRAW: 3, PLAYER: 6}[winner]

    return shape_score + win_score


def main():
    rounds = get_rounds()
    total_score = 0

    for round in rounds:
        total_score += determine_score(*round)
    
    print(total_score)


if __name__ == "__main__":
    main()
