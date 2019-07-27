a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

print(result)


result_re = [num * 4 for num in a]
print(result_re)


result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)
