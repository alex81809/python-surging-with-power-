def is_power_of_eight(n):
    # Powers of 8 must be positive (8^0 = 1)
    if n <= 0:
        return False
    
    # Keep dividing by 8 as long as the remainder is 0
    while n % 8 == 0:
        n //= 8
        
    # If we are left with 1, it's a power of 8
    return n == 1

num = int(input("Enter a number: "))
if is_power_of_eight(num):
    print(f"{num} is a power of 8!")
else:
    print(f"{num} is not a power of 8.")
