def count_substring(string, sub_string):
    list1 = []
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            list1.append(string[i:j+1])
    
    return list1.count(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
