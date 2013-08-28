"""This program is to print a matrix in a spiral order"""
import numpy as np
def printSpiral(M, N, matrix):
    ls = []
    count = M * N
    top_row, bottom_row = 1, M
    first_col, last_col = 1, N
    while count:
        index = first_col
        while count > 0 and index <= last_col:
            ls.append(matrix[top_row-1][index-1])
            index = index + 1
            count = count - 1
        top_row = top_row + 1
        index = top_row
        while count > 0 and index <= bottom_row:
            ls.append(matrix[index-1][last_col-1])
            index = index + 1
            count = count - 1
        last_col = last_col - 1
        index = last_col
        while count > 0 and index >= first_col:
            ls.append(matrix[bottom_row-1][index-1])
            index = index - 1
            count = count - 1
        bottom_row = bottom_row - 1
        index = bottom_row
        while count > 0 and index >= top_row:
            ls.append(matrix[index-1][first_col-1])
            index = index -1
            count = count - 1
        first_col = first_col + 1
    print ls

def main():
    M = int(raw_input("Number of rows: "))
    N = int(raw_input("Number of columns: "))
    matrix = []
    for i in xrange(M):
        ls=[]
        for j in xrange(N):
            ls.append(i * N + j + 1)
        matrix.append(ls)
    print np.array(matrix)
    printSpiral(M, N, matrix)

if __name__ == '__main__':
    main()
