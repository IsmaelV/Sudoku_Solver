# Sudoku Solver 🧠
## Author: Ismael Villegas Molina 🇲🇽 😀
This is a simple sudoku puzzle solver. If you input a valid 
puzzle, we will solve all possible solutions.

The algorithm was written by Professor Thorsten Altenkirch 
on [a YouTube video for Computerphile](https://www.youtube.com/watch?v=G_UYXzGuqvM)
🎥 The rest of the process was written by me. Functions show 
the corresponding author.

### Process 📝
First you run the system (duh). If using an IDE simply press 
the play button. If on the terminal it's as simple as:
```
python sudoku_solver.py
```

#### Constructing sudoku puzzle grid 🔧
First we will be constructing the grid. This will be done 
row-by-row. We will literally be asking each cell one at a 
time for each row. If it's an empty cell, put 0. Otherwise 
put the right number. 

"But Ismael, what if I mess up my input?? 😱" Don't worry! 
That's why we're checking row-by-row so that we can make 
sure that if you mess up the input, you can say you messed up 
and we redo the row 😃

"But Ismael, isn't there a better way to get these inputs? 🤔"
Tbh, yea 😞. Probably could enter the full row all in one go, 
but I wrote this quickly one night when I just 
finished a final (Fight On ✌). I had seen the 
[Computerphile video](https://www.youtube.com/watch?v=G_UYXzGuqvM)
and I was like "yo that's sick" and so I put it on my machine 
and pushed to my profile just in case I wanna use it later. 
Also it was late and I was very sleepy 💤

#### Sit back and relax 😎
Legit, that's it 👌 You did it 🏆 We will provide you with the 
answer to the given puzzle grid and if there is more than one 
solution, we'll give them all to you 💪 free of charge 💚💵