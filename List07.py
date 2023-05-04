def main(list01):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    
    i=0
    n=0
    while i<len(list01):
        if list01[i]==6:
            n=n+1
        i=i+1 
    return n
print(main([2, 6, 2, 2, 6, 2, 2]))