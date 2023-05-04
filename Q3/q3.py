import csv
def main():
    f = open('202303_Seoul_Subway.csv', 'r', encoding='utf-8')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for row in data:
        row = list(map(lambda s : ''.join(s.split()), row))

        if (row[1] == '1호선'):
            arr[0] += int(row[4])
            arr[0] += int(row[5])

        elif (row[1] == '2호선'):
            arr[1] += int(row[4])
            arr[1] += int(row[5])

        elif (row[1] == '3호선'):
            arr[2] += int(row[4])
            arr[2] += int(row[5])

        elif (row[1] == '4호선'):
            arr[3] += int(row[4])
            arr[3] += int(row[5])

        elif (row[1] == '5호선'):
            arr[4] += int(row[4])
            arr[4] += int(row[5])

        elif (row[1] == '6호선'):
            arr[5] += int(row[4])
            arr[5] += int(row[5])

        elif (row[1] == '7호선'):
            arr[6] += int(row[4])
            arr[6] += int(row[5])

        elif (row[1] == '8호선'):
            arr[7] += int(row[4])
            arr[7] += int(row[5])

        elif (row[1] == '9호선'):
            arr[8] += int(row[4])
            arr[8] += int(row[5])

    print("*** Subway Report for Seoul on March 2023 ***")
    
    max = 0
    max_index = 0
    for i in range(9):
        if max < arr[i]:
            max = arr[i]
            max_index = i
    print("1st Busiest Line: Line", (max_index+1), "( %d )" % (max))

    max_2 = 0
    max_2_idx = 0

    for i in range(9):
        if i == max_index:
            continue
        if max_2 < arr[i]:
            max_2 = arr[i]
            max_2_idx = i
    print("2nd Busiest Line: Line", (max_2_idx+1), "( %d )" % (max_2))

    min = max
    min_idx = 0
    for i in range(9):
        if min > arr[i]:
            min = arr[i]
            min_idx = i
    print("1st Least used Line: Line", (min_idx+1), "( %d )" % (min))

    min_2 = max
    min_2_idx = 0

    for i in range(9):
        if i == min_idx:
            continue
        if min_2 > arr[i]:
            min_2 = arr[i]
            min_2_idx = i
    print("2nd Least used Line: Line", (min_2_idx+1), "( %d )" % (min_2))

    f.close()
    
main()
