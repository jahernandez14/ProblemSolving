## Arithmetic Slices

* The purpose of this problem is to find all possible arithmetic combinations of a given array. An arithmetic combination is one that is at least of length three and that all the numbers of the set are the same distance from each other. Example [1,3,4,7,9], this example would produce a result of 6. Like all dynamic problems here the problem is repeated work. The inefficient way to check all routes but by storing the possible routes and storing them. In this particular example the accumulated sum is stored in an array and then returns the sum of all possible arithmetic combinations for a certain element. This example uses recursive elements and returns the sum of the array. 

* In this problem the solution is stored in an array. In addition, it is assumed that the given array is sorted. It iterates through the array and find every combination for each element. It does this by comparing two elements and if they are equal to eachother then it is a valid combination. After this it sums it with the prior entry to have an accumulated sum. The process is repeated to calculate the sum of all counted comparisons.

* g
