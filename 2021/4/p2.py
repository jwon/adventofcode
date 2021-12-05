import sys


def mark_board(board, drawn_number):
    # Mark board if drawn_number is found
    for row in board:
        for col_idx, number in enumerate(row):
            if number == drawn_number:
                row[col_idx] = None

def check_won_horizontally(board):
    for row in board:
        if all(i is None for i in row):
            return True
    return False


def check_won_vertically(board):
    for col_idx in range(len(board[0])):
        if all(row[col_idx] is None for row in board):
            return True
    return False


def check_winning_board(board, drawn_number, won_boards, total_board_count):
    if check_won_horizontally(board) or check_won_vertically(board):
        won_boards.append(board)
        # print(f'{len(won_boards)} won_boards')
    if len(won_boards) == total_board_count:
        return calculate_score(board, drawn_number)
    else:
        return None


def calculate_score(board, winning_number):
    print(f'winning board: {board}')
    return sum(number for row in board for number in row if number is not None) * winning_number


if __name__ == "__main__":
    drawn_numbers = []
    boards = []
    won_boards = []
    current_board = []
    with open('input.txt') as f:
        for line in f:
            if not drawn_numbers:
                drawn_numbers = [int(i) for i in line.strip().split(',')]
            elif line.strip() == '':
                if len(current_board) > 0:
                    boards.append(current_board)
                    current_board = []
            else:
                current_board.append([int(i) for i in line.strip().split()])
        # add the last board to boards
        boards.append(current_board)
    
    total_board_count = len(boards)
    for idx, drawn_number in enumerate(drawn_numbers):
        print(f'#{idx} drawn number: {drawn_number}')
        for board in boards:
            mark_board(board, drawn_number)
            winning_score = check_winning_board(board, drawn_number, won_boards, total_board_count)
            if winning_score is not None:
                print(winning_score)
                sys.exit()
        
        # remove boards that have already won
        boards = [board for board in boards if board not in won_boards]
        print(f'Boards remaining: {len(boards)}')
