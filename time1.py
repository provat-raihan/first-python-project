def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
terms = int(input("Enter the number of terms: "))
print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i))
