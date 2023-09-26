def mat(m):
    rows = len(m)
    columns = len(m[0])

    for j in range(columns):
        neg_col = True
        count = 0
        count_neg_ele = 0

        for i in range(rows):
            if m[i][j] >= 0:
                neg_col = False
                break
            else:
                count += m[i][j]
                count_neg_ele += 1
        if neg_col:
            average = count/count_neg_ele
            return j, average
        return None, None


matrix = [
    [-100, 2, 6],
    [-3, 4, 8],
    [-2, 0, -1]
]

column_index, average_count = mat(matrix)

if column_index is not None:
    print(f"First negative column: {column_index}")
    print(f"Average: {average_count}")
else:
    print("None negative column")
