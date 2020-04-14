"""
    Author of rows from 14 to 71 is Antoine Prudhomme - https://medium.com/@prudywsh
    He has the article about generating big prime numbers on Medium.
    Reference to article - https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
    It is very cool content. I advise to read it.

    And I would like to say thanks for it!!!
"""

from random import randrange, getrandbits, choice
from numpy import gcd


""" Start of Antoine Prudhomme's code. """
def is_prime(n, k=128):

    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """

    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=512):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p
""" The End of Antoine Prudhomme's code. """


def generatePublicKey():
    """ This function for generating Public Key in RSA."""
    # Use not big numbers. We can save some time for multiplication. This numbers have only two '1' in binary view.
    numbers = [3, 17, 65537]

    while True:
        e = choice(numbers)  # choice first part of public key

        q = generate_prime_number()
        p = generate_prime_number()

        n = p * q  # calculate second part of public key

        numberFuncEuler = (q - 1) * (p - 1)  # using Euler's function for getting number of prime numbers < n-1

        if gcd(e, numberFuncEuler) == 1:  # check "Are e and numberFuncEuler mutually Prime numbers?"
            break

    return e, n, numberFuncEuler


def generatePrivateKey(a, p, b=1):
    """ This function for generating Private Key in RSA.
        Use solving comparisons by replacing a variable.
        Change b to b + pk.
    """
    k = 1
    r = gcd(a, p)

    if r != 1:
        p = p // r

    while True:

        if (b + p * k) % a == 0:
            return (b + p * k) // a

        k += 1


def sign(hash, privKey, secondPartPubKey):
    """ This function returns signature, which calculates with helping of existing hash of text or file,
        first part of PubKey and second part of PubKey.

        Arguments in hex view. And we have to format them to decimal view. For successful calculation of hash.
        :argument hash - hash of file or text
    """
    hashInt = int(hash, 16)
    privKey = int(privKey, 16)
    secondPartPubKey = int(secondPartPubKey, 16)
    s = pow(hashInt, privKey, secondPartPubKey)

    return s


def check(signature, firstPartPubKey, secondPartPubKey):
    """ This function returns hash, which calculates with helping of existing signature,
        first part of PubKey and second part of PubKey.

        Arguments in hex view. And we have to format them to decimal view. For successful calculation of hash.
    """
    signature = int(signature, 16)
    firstPartPubKey = int(firstPartPubKey, 16)
    secondPartPubKey = int(secondPartPubKey, 16)
    hash = pow(signature, firstPartPubKey, secondPartPubKey)

    return hash
