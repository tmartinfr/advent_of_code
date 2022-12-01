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
    new_boards = []
    completed_boards = []

    for board in boards:
        board = [
            [
                None if n == num else n
                for n in line
            ] for line in board
        ]

        for line in board + list(zip(*board)):
            if not any(line):
                completed_boards.append(board)
                break
        else:
            new_boards.append(board)

    return new_boards, completed_boards


def count_unmarked(board):
    return sum([n if n else 0 for line in board for n in line])


for num in nums:
    boards, completed_boards = mark_boards(boards, num)
    if not len(boards):
        assert len(completed_boards) == 1
        print(num * count_unmarked(completed_boards[0]))
        exit(0)
