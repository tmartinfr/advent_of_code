lines = open('04a_input', 'r').readlines()
nums = [int(n) for n in lines.pop(0).strip().split(',')]

boards = []
for line in lines:
    line = line.strip()
    if not line:
        board = []
        boards.append(board)
        continue
    board.append([int(n) for n in line.split()])


def mark_boards(boards, num):
    return [
        [
            [
                None if n == num else n
                for n in line
            ] for line in board
        ] for board in boards
    ]


def find_completed(boards):
    for board in boards:
        for line in board + list(zip(*board)):
            if not any(line):
                return board


def count_unmarked(board):
    return sum([n if n else 0 for line in board for n in line])


for num in nums:
    boards = mark_boards(boards, num)
    if completed_board := find_completed(boards):
        print(num * count_unmarked(completed_board))
        exit(0)
