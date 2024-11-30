def get_grid():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    grid = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input("Enter element for [" + str(i) + "][" + str(j) + "]: "))
            row.append(element)
        grid.append(row)
    return grid

def row_sums(grid):
    for i in range(len(grid)):
        row_sum = 0
        for j in range(len(grid[i])):
            row_sum += grid[i][j]
        print("Sum of row " + str(i+1) + " : " + str(row_sum))

def column_sums(grid):
    columns = len(grid[0])
    for j in range(columns):
        column_sum = 0
        for i in range(len(grid)):
            column_sum += grid[i][j]
        print("Sum of column " + str(j+1) + " : " + str(column_sum))


def get_operation_choice():
    print("Choose an operation:")
    print("1. Calculate row sums")
    print("2. Calculate column sums")
    choice = int(input("Enter your choice (1 or 2): "))
    while choice not in [1, 2]:
        print("Invalid choice. Please try again.")
        choice = int(input("Enter your choice (1 or 2): "))
    return choice


def main():
    grid = get_grid()
    choice = get_operation_choice()
    if choice == 1:
        row_sums(grid)
    elif choice == 2:
        column_sums(grid)

if __name__ == "__main__":
    main()
