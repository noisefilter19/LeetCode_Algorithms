# Author : Abinash Gogoi 
MOD = 1000000007
def power_number(base, power):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0

    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """

    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD

        # Divide the power by 2

        power = power // 2

        # Multiply base to itself

        base = (base * base) % MOD

    return result
# Now you can give input as:
# power_number(x,n)
# where x is the base and n is the coefficent
# result will give you the answer
# Happy Coding