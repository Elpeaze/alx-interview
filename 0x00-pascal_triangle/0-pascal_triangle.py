#!/usr/bin/python3

def pascal_triangle(n):
    tringle = []
	for idx in range(n):
        row = []
        for val in range(idx + 1):
            if (val = 0) or (val = idx):
                row.append(1)
            else:
                row.append(triangle[idx - 1][val] + triangle[idx - 1][val - 1])
        triangle.append(row)
    return triangle
