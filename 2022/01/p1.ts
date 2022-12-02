import { readFileSync} from 'fs';

const file: string = readFileSync('./input.txt', 'utf-8');

let highestCaloriesSeen = 0;
let current = 0;
for (const line of file.split('\n')) {
  current = current + +line;

  if (line === '') {
    if (current > highestCaloriesSeen){
    highestCaloriesSeen = current;
    }
    current = 0;
  }
}

console.log(highestCaloriesSeen)
