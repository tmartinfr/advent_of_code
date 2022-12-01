from copy import deepcopy
import sys


def parse_input(filename):
    deck1 = curr_deck = []
    deck2 = []
    for line in open(filename, 'r'):
        line = line.strip()
        if line.startswith('Player'):
            continue
        if line == '':
            curr_deck = deck2
            continue
        curr_deck.append(int(line))
    return [deck1, deck2]

starting_decks = parse_input(sys.argv[1])

def already_played_decks(decks, decks_hist):
    decks_tuple = tuple([tuple(deck) for deck in decks])
    if decks_tuple in decks_hist:
        decks_hist = set()
        return True
    else:
        decks_hist.add(decks_tuple)

def play(cards, decks, recursive, level):
    if recursive and all([card <= len(decks[i]) for i, card in enumerate(cards)]):
        print('Go for recursive game !')
        new_decks = [deck.copy()[:cards[i]] for i, deck in enumerate(decks)]
        return game(new_decks, recursive=True, level=level + 1)[1]
    else:
        best_card = max(cards)
        return cards.index(best_card)

def get_score(decks, winning_player):
    return sum([(index + 1) * card for index, card in enumerate(reversed(decks[winning_player]))])

def game(starting_decks, recursive=False, level=1):
    decks = deepcopy(starting_decks)
    decks_hist = set()

    if recursive:
        print(f'Starting game level {level}')

    if not all(decks):
        raise AssertionError('Game cannot be launched with an empty deck')

    while(all(decks)):
        for i, deck in enumerate(decks):
            print(f'Player {i} deck : {deck}')

        cards = []

        if recursive and already_played_decks(decks, decks_hist):
            print(f'Deck already player, interrupting game {level}')
            return decks, 0

        for i, deck in enumerate(decks):
            card = deck.pop(0)
            print(f'Player {i} plays {card}')
            cards.append(card)

        winning_player = play(cards, decks, recursive, level)
        print(f'Player {winning_player} wins !')
        winning_card = cards[winning_player]
        other_cards = [card for i, card in enumerate(cards) if i != winning_player]
        decks[winning_player].extend([winning_card, *other_cards])

    return decks, winning_player

decks, winning_player = game(starting_decks)
score = get_score(decks, winning_player)
assert score == 31809
print(f'Score (part 1) is {score}')

decks, winning_player = game(starting_decks, recursive=True)
score = get_score(decks, winning_player)
print(f'Score (part 2) is {score}')
