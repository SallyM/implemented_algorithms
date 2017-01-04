def karatsuba(num1, num2):
    '''
    Multiplies two large numbers
    INPUT: integer, integer - numbers to be multiplied
    OUTPUT: integer - product of two input numbers
    '''

#   Base case: simply multiply 1-digit numbers together
    if num1 < 10 or num2 < 10:
        return num1 * num2

#   Calculate the size of the numbers
    s_num1 = str(num1)
    s_num2 = str(num2)
    size_num1 = len(s_num1)
    size_num2 = len(s_num2)
    m = max(size_num1, size_num2)
    m2 = m/2
#   Split the digit sequences about the middle
    high1 = num1 / 10 ** m2
    low1 = num1 % 10 ** m2
    high2 = num2 / 10 ** m2
    low2 = num2 % 10 ** m2

#   Call function recursively to calculate 3 products & return the answer     
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1),(low2 + high2))
    z2 = karatsuba(high1, high2)
    product = z2 * (10 ** (2 * m2)) + ((z1 - z2 -z0) * (10 ** (m2))) + z0
    return product
