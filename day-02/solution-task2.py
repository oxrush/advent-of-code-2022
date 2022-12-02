
ROCK, PAPER, SCISSORS = 0, 1, 2
OPPONENT, PLAYER, DRAW = 0, 1, 2


def get_rounds():
    rounds = []

    with open("input.txt") as file:
        for line in (line.strip() for line in file if line.strip() != ""):
            opponent = {"A": ROCK, "B": PAPER, "C": SCISSORS}[line[0]]
            winner = {"X": OPPONENT, "Y": DRAW, "Z": PLAYER}[line[2]]
            rounds.append((opponent, winner))

    return rounds


def determine_player_shape(opponent, winner):
    return {
        (ROCK, DRAW): ROCK,
        (ROCK, PLAYER): PAPER,
        (ROCK, OPPONENT): SCISSORS,
        (PAPER, OPPONENT): ROCK,
        (PAPER, DRAW): PAPER,
        (PAPER, PLAYER): SCISSORS,
        (SCISSORS, PLAYER): ROCK,
        (SCISSORS, OPPONENT): PAPER,
        (SCISSORS, DRAW): SCISSORS
    }[(opponent, winner)]


def determine_score(opponent, winner):
    player = determine_player_shape(opponent, winner)
    shape_score = {ROCK: 1, PAPER: 2, SCISSORS: 3}[player]

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
