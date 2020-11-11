import sys
if __name__ == '__main__':
    input_param = sys.argv[1]
    with open(input_param, 'r') as data:
        data_dict = {}
        next(data)
        for i in data:
            record = i.rstrip().split("\"")
            if len(record) == 3:
                starting = record[0].split(",")
                ending = record[2].split(",")
                if data_dict.get(starting[7], None) is None:
                    if ending[9] != "(X)":
                        data_dict[starting[7]] = [int(starting[7]), record[1], [starting[0]], int(ending[4]),
                                                  int(ending[6]), float(ending[9])]
                    else:
                        data_dict[starting[7]] = [int(starting[7]), record[1], [starting[0]], int(ending[4]),
                                                  int(ending[6]), 0]
                else:
                    data_dict[starting[7]][2].append(starting[0])
                    data_dict[starting[7]][3] += int(ending[4])
                    data_dict[starting[7]][4] += int(ending[6])
                    if ending[9] != "(X)":
                        data_dict[starting[7]][5] += float(ending[9])
                    else:
                        data_dict[starting[7]][5] += 0

    data.close()

    for item in data_dict:
        data_dict[item][2] = len(set(data_dict[item][2]))
        data_dict[item][5] = round(data_dict[item][5] / data_dict[item][2], 2)

    unsorted_records = []
    for element in data_dict:
        unsorted_records.append(data_dict[element])

    sorted_records = sorted(unsorted_records, key=lambda x: x[0])
    print(sorted_records)
    output_param = sys.argv[2]

    file = open(output_param,'w+')
    for row in sorted_records:
        file.write("{},{},{},{},{},{}\n".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    file.close()