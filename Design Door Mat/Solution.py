# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
pattern = ".|."

for i in range(n):
        pattern = '.|.'
        if i < (n - 1) / 2:
            # Calculate the number of dots and pipes before the center line
            print((pattern * i).center(m, '-'))
        elif i == (n - 1) / 2:
            # Print the center line with the word "WELCOME"
            print('WELCOME'.center(m, '-'))
        else:
            # Calculate the number of dots and pipes after the center line
            print((pattern * (n - 1 - i)).center(m, '-'))


