# #fibanocci series using recursion:


def fibanocci_recursion(n):
   if n <= 1:
       return n
   elif n==2:
       return 1
   else:
       return(fibanocci_recursion(n-1) + fibanocci_recursion(n-2))

nterms = int(input())
if nterms <= 0:
   print("Enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibanocci_recursion(i))
