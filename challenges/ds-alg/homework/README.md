# Homework
Alas, you have procrastinated on your homework too much. Your teacher has threatened to fail you if you don't turn in enough overdue homework by today. More specifically, you currently owe the teachers N units of homework, and by the end of today, you must have exactly M units of homework left.

But all is not lost! You figured you could hire some of your friends to help by bribing them with purple candy while you continue playing games.

For A purple candies they will do one piece of your homework.
For B purple candies they will reduce your entire homework pile by half (rounding down when necessary).

Note that you can never have a negative amount of homework.

Your task now is to produce a sorted table of codenames and their respective minimum costs (in purple candy) to solve your overdue homework problem.

The first line of input consists of a single positive integer representing the number of cases to follow. Each case begins with three positive integers separated by spaces: N - your starting amount of homework, M - your target amount of homework, and L - the number of friends you have, (1 <= M <= N <= 100000, 1 <= L <= 100). The next L lines have the format "[codename]:A,B", where A and B are the rates as described above for the given friend (who is using a code name so they don't get in trouble) (0 <= A,B <= 10000). The length of the codename will be between 1 and 16, will consist only of capital letters, and will be unique.

For each test case, print "Case X", with X being the case number, on a single line, followed by the table of code names and their respective minimum costs, sorted in non-decreasing order of minimum costs. Sort friends with identical minimum costs in alphabetical order by code name. For each line of the table, print out the code name, followed by a space, followed by the minimum required cost for that agency to solve your problem.

##### Sample Input
```
2
100 5 3
A:1,10
B:2,5
C:3,1
1123 1122 5
B:50,300
A:1,1000
C:10,10
D:1,50
E:0,0
```

##### Sample Output
```
Case 1
C 7
B 22
A 37
Case 2
E 0
A 1
D 1
C 10
B 50
```
