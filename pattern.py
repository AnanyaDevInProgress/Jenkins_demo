# Just a pattern code
n = 9
print("My first E2E Jenkins run")
for i in range(n):
  print(" " * (n - i - 1), end="")
  print("*" * (2 * i + 1))
