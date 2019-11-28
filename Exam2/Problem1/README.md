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

* Dynamic problems are very difficult and usually you can tell that there is going to be a dynamic property when you notice repeated work or when multiple loops are required to achieve a result. IDEAL and Dukes 7 steps were essential in coming up with a solution. First all problems are identified. For this problem it was identified that getting TRUE was the desired result. In fact, that is the only result attainable. For this problem it was the creation of the logic that determined if the result was going to be true. Achieving TRUE became my goal. There were many solutions you could store of the computation or do it iteratively, but the most efficient course was employing dynamic programming. I anticipated True but if the logic was flawed it would return false. In doing so it was possible to check when it was false. After the problem was completed it left me thinking on the importance of mathematics. The result was achieved but it demanded for me to think of a way or pattern that would cause player 1 to win. This was the most challenging by far. By using Dukes steps, I broke down the problem and solved a little at a time. Once the correct behavior was seen I would move on. The code is shown on GitHub. By using abstraction, I was able to see that no matter what player 1 wins. It is simple to say just return true but once again I believe the problem was asking for the player logic no the result.
