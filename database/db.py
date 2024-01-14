def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

# Prompt the user for the number of terms in the Fibonacci sequence is sequence
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate and print the Fibonacci sequence
result_sequence = fibonacci_sequence(num_terms)
print("Fibonacci Sequence:", result_sequence)
print("Fibonacci Sequence:", result_sequence)

