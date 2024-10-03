"""
module containing functions to generate pascal traingle
"""


def pascal_triangle(n):
    """function to generate pascal traingle"""
    if n <= 0:
        return ([])
    if not isinstance(n, int):
        print(f'${n} is not a valid input')
        return ([])
    triangle = [[1]]
    if n == 1:
        traingle.append([1, 1])
        return (triangle)

    for row in range(1, n):
        if row == 1:
            triangle.append([1, 1])
        else:
            # print(f'a list {triangle[row - 1]}')
            mid = pick_seq_pairs(triangle[row - 1])
            triangle.append([1] + mid + [1])
    return (triangle)


def pick_seq_pairs(li):
    """picks sequential pairs of a list
        e.g list = [1, 3, 4, 7]
        pairs = [[1, 3], [3, 4], [4, 7]]
    """
    items = len(li)
    pairs = []
    for i in range(items - 1):
        # print(f'[{i}, {i + 1}]')
        pairs.append(li[i] + li[i + 1])
    # print(pairs)
    return (pairs)

# pick_seq_pairs([1, 3, 4, 7, 8])
