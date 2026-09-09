def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number >= 1:
        divisors_total = 0
        for num in range(1,(number//2)+1):
            if number % num == 0:
                divisors_total += num
    if divisors_total == number:
        return "perfect"
    if divisors_total > number:
        return "abundant"                
    if divisors_total < number:
        return "deficient"         






    
