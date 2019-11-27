## Stone Game

* This problem immediately displays a need for dynamic programming. In order to win the player must consider the 
multiple options and routes to take in order to win. Its proven mathematically that as long as player one makes the 
best choice and goes first, he will win. The role of the recursive call is to select the best option, store it, and 
reuse it as the game progresses. The problem is that the player does not want to recalculate his moves every time his 
turn appears. In order to select the best, move he must assess all possible routes and selections before making a choice. 
Ideally, choosing the largest would work but unfortunately this doesn’t consider the values in between. In order to address 
this problem, the inputs are compared and passed recursively until the most efficient router is uncovered.

* This problem does not use an assigned data structure. Instead it is using a stack. It stores the compared value 
on the stack and calls a recursive call based on the if statement met. It recurses down the array checking the best 
values checking from the inside to the outside.

* G
