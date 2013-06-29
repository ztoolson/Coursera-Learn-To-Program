def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    # Minimum number of buses requires is 1 based off precondition
    return 1 + (n // 50)


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    sum_of_gains = 0
    sum_of_losses = 0

    for element in price_changes:
        if element > 0:
            sum_of_gains += element #gains are positive changes
        else:
            sum_of_losses += element #losses are negative changes

    return (sum_of_gains, sum_of_losses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    # Create a list that swaps the elements
    #copy_list = end elements + middle elements + beginning elements 
    copy_list = L[-k:] + L[k:-k] + L[:k] 

    #update the original list L
    for i in range(len(L)):
        L[i] = copy_list[i]
        
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
