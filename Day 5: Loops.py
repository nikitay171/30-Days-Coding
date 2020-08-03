Given an integer, , print its first 10 multiples. Each multiple n*i (where 1<i<=10) should be printed on a new line in the form: n x i = result.

----------------------------------------------------
n = int(input())
for i in range(1,11):
    print('{0} x {1} = {2}'.format(n, i, n*i))
