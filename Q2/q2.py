import csv
def main():
    f = open('2022_Seoul_Temp.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    dif_max = 0.0
    dif_max_day = ''
    dif_min = 1000.0
    dif_min_day = ''
    for row in data:
        row = list(map(lambda s : ''.join(s.split()), row))
        if not (row[3] == '') and not (row[4] == ''):
            d_min = float(row[3])
            d_max = float(row[4])
            if dif_max < (d_max - d_min):
                dif_max = d_max - d_min
                dif_max_day = row[0]
            if dif_min > (d_max - d_min):
                dif_min = d_max - d_min
                dif_min_day = row[0]

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation:", dif_max_day)
    print("Maximum Temperature Difference: %.1f" % (dif_max), "Celsius")
    print("Day with the Smallest Temperature Variation:", dif_min_day)
    print("Minimum Temperature Difference: %.1f" % (dif_min), "Celsius")
    f.close()

main()
