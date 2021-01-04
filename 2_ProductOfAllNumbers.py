def prod_num(numbers):
    """
    Return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i (Division)
    """
    prefix_products = []
    for number in numbers:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * number)
        else:
            prefix_products.append(number)

    suffix_products = []
    for number in reversed(numbers):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * number)
        else:
            suffix_products.append(number)
    suffix_products = list(reversed(suffix_products))

    # print(prefix_products)
    # print(suffix_products)

    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(numbers) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])
    
    return result

lst1 = [1, 2, 3, 4, 5]
print(prod_num(lst1))

lst2 = [3, 2, 1]
print(prod_num(lst2))

