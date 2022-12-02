import { readFileSync} from 'fs';

const file: string = readFileSync('./input.txt', 'utf-8');
const guide: string[][] = file.trim().split('\n').map(l => l.split(' '))
const point_map: Record<string, number> = {
  'rock': 1,
  'paper': 2,
  'scissors': 3
}
const opponent_map: Record<string, string> = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors'
}

const my_map: Record<string, string> = {
  'X': 'rock',
  'Y': 'paper',
  'Z': 'scissors'
}

function round_outcome(my_move: string, opponent_move: string): number {
  if (my_move === opponent_move) {
    return 3;
  } else if ((my_move === 'rock' && opponent_move === 'scissors') ||
  (my_move === 'scissors' && opponent_move === 'paper') ||
  (my_move === 'paper' && opponent_move === 'rock')) {
    return 6;
  } else {
    return 0;
  }
}

console.log(guide.map(round => {
  const [opponent, me] = round;
  const my_move = my_map[me]
  console.log(my_move)
  const opponent_move = opponent_map[opponent]
  console.log(opponent_move)
  console.log(point_map[my_move])
  console.log(round_outcome(my_move, opponent_move))
  console.log(point_map[my_move] + round_outcome(my_move, opponent_move))
  return point_map[my_move] + round_outcome(my_move, opponent_move)
}).reduce((sum, current) => sum + current, 0));
