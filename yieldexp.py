def show(n):
    i=1
    while i<n:
        yield i
        i=i+1


r=show(10)
print(r)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
try:
    print(next(r))
except StopIteration:
    print("please stop ")




