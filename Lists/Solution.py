lst = []

    command_map = {
        'insert': lambda x: lst.insert(int(x[1]), int(x[2])),
        'print': lambda x: print(lst),
        'remove': lambda x: lst.remove(int(x[1])),
        'append': lambda x: lst.append(int(x[1])),
        'sort': lambda x: lst.sort(),
        'pop': lambda x: lst.pop(),
        'reverse': lambda x: lst.reverse()
    }

    for _ in range(N):
        command = input().split()
        command_map[command[0]](command)
