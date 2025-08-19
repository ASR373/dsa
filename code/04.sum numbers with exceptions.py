Calculate the sum from 0 to a given number N, excluding numbers that are divisible by 3 and 7.

Constraints
The input variable N must be an integer.
N must be non-negative.
N can be any positive integer, including zero.


solution:

  def calculate_sum(N):
    """ 
    :type N: int
    :rtype: int
    """
    sum = 0
    for i in range(0,N+1):
        if i % 3 != 0 and i % 7 != 0:
            sum+=i
            
    return sum
