# built-in sorting algorithm

list = [5, 45, 22 , 3, 9, 0, 12, 6, 1]
 
print(sorted(list))
# prints [0, 1, 3, 5, 6, 9, 12, 22, 45]

# bubble sort
# initial list, compare 29 & 10
[29, 10, 15, 32, 10]
# 29 > 10, so we swap & compare 29 & 15
[10, 29, 15, 32, 10]
# 29 > 15, so we swap & compare 29 & 32
[10, 15, 29, 32, 10]
# 29 < 32, so we compare 32 & 10
[10, 15, 29, 32, 10]
# 32 > 10, so we swap
[10, 15, 29, 10, 32]
# Begin again from the first element, compare 10 & 15
[10, 15, 29, 10, 32]
# 10 < 15, so we compare 15 & 29
[10, 15, 29, 10, 32]
# 15 < 29, so we compare 29 & 10
[10, 15, 29, 10, 32]
# 29 > 15, so we swap & compare 29 & 32
[10, 15, 10, 29, 32]
# Begin again, from the first element compare 10 & 15
[10, 15, 10, 29, 32]
# 10 < 15, so we compare 15 & 10
[10, 15, 10, 29, 32]
# 15 > 10, so we swap
[10, 10, 15, 29, 32]
# Begin again from the first element, list is now sorted
[10, 10, 15, 29, 32]


# Merge sort
def recursive(n):
    # This is the base case we are working towards
    # When we get to where n==0, we return 1
    if n == 0:
        return 1
    # here we move towards the base case
    return n * recursive(n - 1)