# Homework
This problem is taken from [here](https://open.kattis.com/problems/reduction).

## Solution
A greedy solution suffices. For each friend, add up the minimum cost (using either A or B) to half workload N as long as the result will not fall below M. Afterwards, just add up the costs using A to reach M. Output the formatted sorted ordered pairs of (cost, name) for each friend.

## Proof
Let's attempt to prove the answer will be given by a sequence of Bs followed by a sequence of As by contradiction.

Suppose otherwise, then there must exist a sequence of n As that occurs before a B (...A...AB...) in the optimal solution.
Let the amount of homework before the first A in such a sequence be X. Then the final amount of homework will be `Y = floor((X-nA)/2) = floor(X/2 - nA/2)`, and the cost will `nA + B`.
If we were to move B before all the As, the final amount of homework will be `Y' = floor(X/2) - nA`. With some simple manipulation, we can easily see that `Y' <= Y` (proof is left as an exercise to the reader). Furthermore, since `floor(X/2) >= floor((X-nA)/2)`, `Y'+nA >= Y`. Thus, we can remove some As at the end to construct a solution with a reduced cost.  Since we can't improve the optimal solution, this is a contradiction. Hence, no such sequence must exist.