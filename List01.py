def main(fruits,x):
    """
    You will be given a list of fruits. Add x fruit to it from the end and return.
    Args:
        fruits(list): parameter 
        x(str): parameter
    Returns:
        list: return answer
    """
    s=fruits.append(x)
    return fruits
print(main(["apple", "pear"],"kiwi"))