elements = [1, 2, 3, 4, 5, 6, 6, 7]
exclude = [1, 3, 6]
result = [e for e in elements if e not in exclude]
print(result)