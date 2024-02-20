if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(set(arr))
    arr_list.remove(max(arr_list))
    runner_up = max(arr_list)
    print(runner_up)
    
