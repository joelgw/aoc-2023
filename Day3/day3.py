def main():
    with open("input.txt") as file:
        infile = file.readlines()

    challenge1(infile)

def make_matrix(infile):
    matrix = []
    rows = 0
    cols = 0
    for line in infile:
        matrix.append(line.strip())
        rows += 1
        cols = len(line.strip())
    return matrix, rows, cols

#Finds the next number available in the matrix
#Starts looking at the specified position in the matrix
def get_next_number(matrix, row, col, max_row, max_col):
    r = row
    c = col
    # Step through matrix looking for digits
    while not matrix[r][c].isdigit():
        if c < max_col - 1:
            c += 1
        elif c == max_col - 1 and r < max_row - 1:
            c = 0
            r += 1
        else:
            print("End of matrix")
            break

    #Should have found the starting digit of the next number to evaluate
    # Will only be on the same row, no need to increment row
    c2 = c
    print(matrix[r].split())
    while matrix[r][c2].isdigit():
        if c2 != max_col - 1:
            c2 += 1
        else:
            break

    # r is the starting position of the digit, r2 is the ending position
    num = ""
    #if c2 == max_col - 1:
    #    c2 += 1
    for x in range(c2-c):
    #    if matrix[r][c+x] != '.':
        num += matrix[r][c + x]
    #if c2 == max_col:
    #    c2 -= 1

    ret_c = c
    ret_r = r
    #Edge case where number was at the end of the line, row needs to increment
    if c2 == max_col - 1:
        ret_c = 0
        ret_r = r + 1
    else:
        ret_c = c2 + 1
    if num == "":
        num = None
    else:
        num = int(num)
    return num, r, c, ret_r, ret_c

def check_symbol_adjacent(mtx, num, pos_r, pos_c, max_row, max_col):
    #Checks all grid spaces adjacent to number for symbols other than .
    is_valid = False

    def symbol(c):
        if not c.isdigit() and c != '.':
            return True

    #Check row above
    if pos_r != 0:
        for i in range(pos_c, pos_c + len(str(num)), 1):
            if symbol(mtx[pos_r - 1][i]):
                return True

    # Check row below
    if pos_r != max_row - 1:
        for i in range(pos_c, pos_c + len(str(num)), 1):
            if symbol(mtx[pos_r + 1][i]):
                return True

    # Check left
    if pos_c != 0:
        if symbol(mtx[pos_r][pos_c - 1]):
            return True

    # Check Right
    if pos_c != max_col - 1:
        if symbol(mtx[pos_r][pos_c + len(str(num))]):
            return True

    # Check Top Left
    if pos_r != 0 and pos_c != 0:
        if symbol(mtx[pos_r - 1][pos_c - 1]):
            return True

    #Check Top Right
    if pos_r != 0 and pos_c != max_col - 1:
        if symbol(mtx[pos_r - 1][pos_c + len(str(num))]):
            return True

    #Check Bottom Left
    if pos_r != max_row - 1 and pos_c != 0:
        if symbol(mtx[pos_r + 1][pos_c - 1]):
            return True

    # Check Bottom Right
    if pos_r != max_row - 1 and pos_c != max_col - 1:
        if symbol(mtx[pos_r + 1][pos_c + len(str(num))]):
            return True

def challenge1(infile):
    mtx, rows, cols = make_matrix(infile)

    nums = []
    num, pos_r, pos_c, next_r, next_c = get_next_number(mtx, 0, 0, rows, cols)
    if num:
        if check_symbol_adjacent(mtx, num, pos_r, pos_c, rows, cols):
            nums.append(num)
    while next_r != rows:
        num, pos_r, pos_c, next_r, next_c = get_next_number(mtx, next_r, next_c, rows, cols)
        if num:
            if check_symbol_adjacent(mtx, num, pos_r, pos_c, rows, cols):
                nums.append(num)

    print(nums)
    print(sum(nums))

if __name__ == "__main__":
    main()
