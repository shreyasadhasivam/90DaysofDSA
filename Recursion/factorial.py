def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
num = 6
if num < 0:
  print("Invalid input ! Please enter a positive number.")
elif num == 0:
  print("Factorial of number 0 is 1")
else:
  print("Factorial of number", num, "=", factorial(num))