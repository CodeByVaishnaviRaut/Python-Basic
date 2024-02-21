if __name__ == '__main__':
    N = int(input())
    list1 = []
    command_map = {
        'insert':lambda x:list1.insert(int(x[1]),int(x[2])),
        'print': lambda x: print(x),
        'remove': lambda x: list1.remove(int(x[1])),
        'append':lambda x: list1.append(int(x[1])),
        'sort':lambda x: list1.sort(),
        'pop':lambda x: list1.pop(),
        'reverse':lambda x: list1.reverse()
    }
    
    for i in range(N):
        command = input().split()
        command_map[command[0]](command)
    
