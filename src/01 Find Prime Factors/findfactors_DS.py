def get_prime_factors(num_to_factor):
    divisor = 2
    factors = []
    while divisor <= num_to_factor:
        if num_to_factor % divisor == 0:
            factors.append(divisor)
            num_to_factor = num_to_factor // divisor
        else:
            divisor += 1

    return factors


if __name__ == '__main__':
    print(get_prime_factors(630))
    print(get_prime_factors(13))
    print(get_prime_factors(1971))
