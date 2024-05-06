def check_prime(n):
    prime = True
    if n <= 2:
        prime = False
    for i in range(2,n):
        if n % i == 0:
            prime = False
    if prime:
        print("This is a prime number")
    else: 
        print("This is not a prime number")
n = int(input("Enter number to check: "))
check_prime(n)