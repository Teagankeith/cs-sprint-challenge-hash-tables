def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    

    for i in arrays:
        for d in i:
            if d in dict:
                dict[d] += 1
            else:
                dict[d] = 1

    results = [i[0] for i in dict.items() if i[1] == len(arrays)]  
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
