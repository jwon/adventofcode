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

const outcome_map: Record<string, string> = {
  'X': 'lose',
  'Y': 'draw',
  'Z': 'win'
}
const move_to_win: Record<string, string> = {
  'rock': 'paper',
  'paper': 'scissors',
  'scissors': 'rock'
}

const move_to_lose: Record<string, string> = Object.entries(move_to_win).reduce((ret: Record<string, string>, entry) => {
  const [key, value] = entry;
  ret[value] = key;
  return ret;
  }, {})

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

function determine_my_move(opponent_move: string, outcome: string): string {
  if (outcome === 'draw') {
    return opponent_move;
  } else if (outcome === 'win') {
    return move_to_win[opponent_move]
  } else {
    return move_to_lose[opponent_move]
  }
}

console.log(guide.map(round => {
  console.log('---')
  const [opponent_code, outcome_code] = round
  const outcome = outcome_map[outcome_code]
  console.log(outcome)
  const opponent_move = opponent_map[opponent_code]
  console.log(opponent_move)
  const my_move = determine_my_move(opponent_move, outcome)
  console.log(my_move)
  console.log(point_map[my_move] + round_outcome(my_move, opponent_move))
  return point_map[my_move] + round_outcome(my_move, opponent_move)
}).reduce((sum, current) => sum + current, 0));
