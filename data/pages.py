# Estimate how many days each chapter should take
import math

p1 = [3, 15, 23, 39, 69, 103, 153]
p2 = [161, 199, 243, 267, 291, 353]
p3 = [365, 387, 397, 413, 437, 451]
N = 10 # Pages per day

def printbook(p):
	for i in range(1, len(p)):
		diff = p[i] - p[i-1]
		print(f"Chapter {i}: {diff} pages, {int(math.ceil(diff/N))} days")

print("Book 1")
printbook(p1)

print("Book 2")
printbook(p2)

print("Book 3")
printbook(p3)