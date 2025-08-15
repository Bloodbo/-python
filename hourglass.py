a = int(input('a = '))

b = 4

for i in range(a, b - 1, -2):

   s2 = 18 - i

   print(" " * (s2// 2), "*" * i)

for i in range(b,a + 1, 2):

   s1 = 18 - i

   print(" " * (s1 // 2), "*" * i)