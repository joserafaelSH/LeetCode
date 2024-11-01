## To this problem we have some approaches

- 1: The first one is the brute force, this is the worst solution but can work or get up a time limit exception. - Time complexity O(n2) Space Complexity (O(1))
- 2: Count the frequency of each numbers from input array, this is a good approach but you want to use one data structure to save and get the frequency
of input values without lose performance. Here you can use a HashMap with ith number as key and your current frequency as value, if the current
number exists in HashMap means that is not unique in the input, - Time complexity O(n) Space Complexity O(n)
- 3: Sort the input array in non-decreasing order and check if the ith number is equal to an i-1th number. Be careful with your sort algorithm, the mergesort
can be a good one. - Time complexity O(n log n - mergesort) (complexity of your sort algorithm) Space Complexity O(1)