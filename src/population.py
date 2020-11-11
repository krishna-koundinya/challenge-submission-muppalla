""" This program takes in the population census data from
(https://www.census.gov/data/tables/time-series/dec/metro-micro/tract-change-00-10.html)
in CSV format and writes, the average population percent change for a particular Core Based Statistical Area (CBSA)
along with other relevant information, to a CSV file.
To run the program use the following command in the terminal
python3.8 population.py path/to/input/file/input.csv path/to/output/file/output.csv"""

# import statements
import sys

# Beginning of the program
if __name__ == '__main__':

    # Creating a variable to read the input csv file
    input_param = sys.argv[1]
    with open(input_param, 'r') as data:

        # Creating a dictionary to keep track of the CBSA
        data_dict = {}

        # Ignoring the header of the csv file
        next(data)
        for i in data:

            # Splitting each line at the double quote to get three parts of each row in data
            # because the CSBA title contains a comma.
            # First Part: data columns before the CSBA title
            # Second Part: the CSBA title column
            # Third Part: data columns after CSBA title
            record = i.rstrip().split("\"")

            # Observation: The absence of CSBA data creates records of length 1
            # The presence of CSBA data creates records of length 3
            if len(record) == 3:

                # Splitting the First Part at commas to get necessary columns
                starting = record[0].split(",")

                # Splitting the First Part at commas to get necessary columns
                ending = record[2].split(",")

                # If there is no CSBA code in the dictionary we add it to the dictionary with the following columns
                # CSBA code, CSBA title, GEO code to count the instances, Population in 2000, Population in 2010
                # Percent change in population
                # The key of the dictionary is CSBA code and the value is a list containing the above columns in that
                # order
                if data_dict.get(starting[7], None) is None:

                    # In case the population change is zero we read an "(X)"
                    # then we add a zero to out list
                    if ending[9] != "(X)":
                        data_dict[starting[7]] = [int(starting[7]), record[1], [starting[0]], int(ending[4]),
                                                  int(ending[6]), float(ending[9])]
                    else:
                        data_dict[starting[7]] = [int(starting[7]), record[1], [starting[0]], int(ending[4]),
                                                  int(ending[6]), 0]

                # In case we already have the CSBA code in our dictionary we add the following
                # GEO code, Population in 2000, Population in 2010 and Percent change in population
                else:
                    data_dict[starting[7]][2].append(starting[0])
                    data_dict[starting[7]][3] += int(ending[4])
                    data_dict[starting[7]][4] += int(ending[6])
                    if ending[9] != "(X)":
                        data_dict[starting[7]][5] += float(ending[9])
                    else:
                        data_dict[starting[7]][5] += 0

    # Closing the data file after reading all the records
    data.close()

    # Modifying the data to create desired output with average population percent change
    for item in data_dict:
        data_dict[item][2] = len(set(data_dict[item][2]))
        data_dict[item][5] = round(data_dict[item][5] / data_dict[item][2], 2)
        data_dict[item][1] = "\""+data_dict[item][1]+"\""

    # Creating a list of lists from the dictionary to sort the data
    unsorted_records = []
    for element in data_dict:
        unsorted_records.append(data_dict[element])

    # Sorting the data based on the CSBA code in ascending order
    sorted_records = sorted(unsorted_records, key=lambda x: x[0])
    # print(sorted_records)
    output_param = sys.argv[2]

    # Using the second parameter to create an output csv file
    file = open(output_param,'w+')
    for row in sorted_records:
        file.write("{},{},{},{},{},{}\n".format(row[0], row[1], row[2], row[3], row[4], row[5]))

    # Closing the file after the completion of usage
    file.close()