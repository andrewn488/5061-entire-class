"""week 8 warmup exercises and videos
"""

iso = {1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu',
       5: 'Fri', 6: 'Sat', 7: 'Sun'}
counts = {}
for key in iso:
    counts[iso[key]] = 0
print(counts)


def who_has_s(d, s):
    for keys in d.keys():
        for values in s.values():
            if 's' in values:
                return values
            return values[keys]


        
