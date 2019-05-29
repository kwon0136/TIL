lunch = {
    '한식집': '02-',
    '중식집' : '031-',
    '일식집' : '054-'
}

# 4-1. 기본
for key in lunch:
    print(key) # key
    print(lunch[key]) # value

# 4-2. key 기본
for key in lunch.keys(): # --> ['한식집', ...]
    print(key)

# 4-3. value 반복
for value in lunch.values(): # --> ['02-', '031-', ...]
    print(value)

# 4-4. key, value 반복
for key, value in lunch.items(): # --> [('한식집, '02-'), ...]
    print(key)
    print(value)
