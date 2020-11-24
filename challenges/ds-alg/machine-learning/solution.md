# Machine-Learning
This problem is original.

## Solution
Both solutions involve the use of line-sweep. Note that python may be too slow for this specific task.

For the first subtask, we can sort all pairs of (p,r) by p and process in increasing p. Maintain a set (or BST) of r values. When we attempt to insert a new point, we remove the points already in the set with an r smaller than or equal to the current point's r. This can be done using binary search (or `lower_bound` in C++). Of course, we need to compare the indices as well if both points happen to be identical. This gives us an O(N log N) complexity, which suffices to pass.

For the second subtask, we need to make an important observation: the r value of the final points are non-decreasing as p increases. Hence, instead of a set, we can use a monotonic stack. When we add a new point, we pop all elements in the stack with a smaller or equal r value. In addition, we will need to use counting sort for the initial and final sorting to cut the log factor. These optimisations will give us a complexity of O(MAX_N + MAX_X) where X is the maximum possible value for p_i and r_i, which suffices to pass this subtask.

