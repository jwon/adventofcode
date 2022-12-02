import { readFileSync} from 'fs';

const file: string = readFileSync('./input.txt', 'utf-8');

const elfCalories: number[] = [];
let current = 0;
for (const line of file.split('\n')) {
  current = current + +line;

  if (line === '') {
    elfCalories.push(current)
    current = 0;
  }
}


console.log(elfCalories.sort((a, b) => b - a).slice(0, 3).reduce((sum, current) => sum + current, 0));
