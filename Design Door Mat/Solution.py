def print_door_mat(n, m):
    pattern = ".|."
    welcome_line = "WELCOME"

    for i in range(n):
        if i < (n - 1) // 2:
            # Calculate the number of dashes on each side of the pattern
            dashes = (m - (len(pattern) * (2 * i + 1))) // 2
            print("-" * dashes + pattern * (2 * i + 1) + "-" * dashes)
        elif i == (n - 1) // 2:
            # Calculate the number of dashes on each side of the "WELCOME" line
            dashes = (m - len(welcome_line)) // 2
            print("-" * dashes + welcome_line + "-" * dashes)
        else:
            # Calculate the number of dashes on each side of the pattern
            dashes = (m - (len(pattern) * (2 * (n - 1 - i) + 1))) // 2
            print("-" * dashes + pattern * (2 * (n - 1 - i) + 1) + "-" * dashes)


# Example: Size 7 x 21
n,m = map(int,input().split())
print_door_mat(n,m)
