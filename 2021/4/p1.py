import sys


def mark_board(board, drawn_number):
    # Mark board if drawn_number is found
    for row in board:
        for col_idx, number in enumerate(row):
            if number == drawn_number:
                row[col_idx] = None


def check_winning_board(board, drawn_number):
    # Check if board won
    # Check if won horizontally
    for row in board:
        if all(i is None for i in row):
            return calculate_score(board, drawn_number)
    # Check if won vertically
    for col_idx in range(len(board[0])):
        if all(row[col_idx] is None for row in board):
            return calculate_score(board, drawn_number)

    return None


def calculate_score(board, winning_number):
    print(f'winning board: {board}')
    return sum(number for row in board for number in row if number is not None) * winning_number


if __name__ == "__main__":
    drawn_numbers = []
    boards = []
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
    
    # print(drawn_numbers)
    # for board_idx, board in enumerate(boards):
    #     print(f'Board #{board_idx}: {len(board)} rows')
    #     for row_idx, row in enumerate(board):
    #         print(f'Row #{row_idx}: {len(row)} columns')

    for idx, drawn_number in enumerate(drawn_numbers):
        print(f'#{idx} drawn number: {drawn_number}')
        for board in boards:
            mark_board(board, drawn_number)
            winning_score = check_winning_board(board, drawn_number)
            if winning_score is not None:
                print(winning_score)
                sys.exit()
