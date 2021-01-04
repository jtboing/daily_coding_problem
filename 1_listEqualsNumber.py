from bisect import bisect_left

def listEqualNumber(numbers, k):
    """
    Returns whether any two numbers from a list add up to k (Brute force)
    """

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if (i != j and numbers[i] + numbers[j] == k):
                return True
        
    return False

numbers = [6, 7, 8, 9]
k = 17

listEqualNumber(numbers, k)

def listEqualNumber2(numbers, k):
    """
    Returns whether any two numbers from a list add up to k (Set)
    """
    seen = set()

    for number in numbers:
        if number - k in seen:
            return True
        seen.add(number)
    return False

def listEqualNumber3(numbers, k):
    """
    Returns whether any two numbers from a list add up to k (Binary search)
    """

    numbers.sort()

    for i in range(len(numbers)):
        target = k - numbers[i]
        j = binarySearch(numbers, target)

        # Check that binary search found the target and that it's not in the same index
        # as i. If it is in the same index, we can check numbers[i + 1] and numbers[i - 1] to see
        #  if there's another number that's the same value as numbers[i].
        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(numbers) and numbers[j + 1] == target:
            return True
        elif j - 1 >= 0 and numbers[j - 1] == target:
            return True
    return False

    

def binarySearch(lst, target):
    low = 0
    high = len(lst)
    ind = bisect_left(lst, target, low, high)

    if 0 <= ind < high and lst[ind] == target:
        return ind
    return -1