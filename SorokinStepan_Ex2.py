from collections import defaultdict

with open('Log.txt', 'r') as f:
    d = {}
    count = 0
    for line in f:
        if len(line) > 38:
            if line[37] == '[':
                d.setdefault(line[26:36].rstrip(), defaultdict(lambda: 0))
                d[line[26:36].rstrip()][line[38:45].rstrip()] += 1
        count += line.count('fun:')
    print('The number of "fun": {}'.format(count))
    for i in d:
        d[i] = dict(d[i])
    print(d)
