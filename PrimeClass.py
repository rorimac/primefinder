# -*- coding: utf-8 -*-
from __future__ import division
import scipy as sp


class PrimeClass(object):
    """
    A class that finds all the primes up to a specified number

    input
    -----

    max_number: A positive number larger than or equal to 2
    """

    def __init__(self, max_number):
        
        # Check that max_number is well behaved.
        if not type(max_number) in [int, float]:
            raise Exception('Your input has to be an integer or a float')
        if max_number <= 2:
            raise Exception('The number you specify has to be larger than 2')
        self.max_number = max_number

    def erathosthenes(self):
        """
        A simple deterministic prime finding algorithm developed in ancient times.
        """

        # Initialize an array containing all integers between 2 and self.maxnumber, including the integer part of self.maxnumber
        # Use only integer part of self.maxnumber
        prime_list = sp.array(range(2,int(self.max_number) + 1))
        
        # When we can terminate the sieve
        stop_value = sp.sqrt(self.max_number)

        for i in range(int(self.max_number)):
            # find the indices of the integers divisible by prime_list[i] 
            nonprime_indices = sp.where(prime_list%prime_list[i] == 0)

            # Disregard first index as it belongs to the prime prime_list[i] and remove numbers belonging to the indices
            nonprime_indices = nonprime_indices[0][1:]
            prime_list = sp.delete(prime_list, nonprime_indices)

            if prime_list[i] > stop_value:
                break

        return prime_list
