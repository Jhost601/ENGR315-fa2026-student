import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###

    a0 = 1 # sets initial value for a0
    b0 = 1 / math.sqrt(2) # sets initial value for b0
    t0 = 1 / 4 # sets initial value for t0
    p0 = 1 # sets initial value for p0
    pi = 0 # sets initial value for pi

    while abs(math.pi - pi) >= target_error: # while loop for iterating until the error is less than the target 

        a = (a0 + b0) / 2 # imports equation for "a" from the Gauss-Legendre algorithm
        b = math.sqrt(a0 * b0) # imports equation for "b" 
        p = 2 * p0 # imports equation for "p"
        t = t0 - p0 * (a0 - a) ** 2 # imports equation for "t"
        pi = ((a + b) ** 2) / (4 * t) # imports equation for "pi"

        a0 = a # sets new value for a0
        b0 = b # sets new value for b0
        p0 = p # sets new value for p0
        t0 = t # sets new value for t0

    # change this so an actual value is returned
    return pi




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
