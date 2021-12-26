def main(a):
    """
    Check the logic "The variable "a" is an even number"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return (a+1)%2
x=main(13)
print(bool(x))