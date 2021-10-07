'''
This script takes a csv file and adds double quotes to each value.

Input:
########
    * -i : CSV file to quote

Output:
########
    * -o : path and file name of the quoted CSV file

Usage:
########
    * python quote_csv.py -h

    *Gives a description of the commands -i and -o

    * python quote_csv.py -i <path/input_filename.csv> -o <path/output_filename.csv>
    
    *Runs the script with the given input and output
'''

import csv
import argparse

def main(csv_file, output_file):
    '''
    Loads CSV file into pandas dataframe, adds quotes, then writes output CSV file
    '''

    # Read the original csv file and load data into a list.
    with open(csv_file, 'r', encoding='utf-8', errors='ignore') as file:
        original_file = csv.reader(file)

        # Create a list to hold the data.
        data = []

        # Add to the data list.
        for row in original_file:
            data.append(row)

    # Write data list to the new file with quotes around all values.
    with open(output_file, 'w') as out_file:
        writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)

    # Output message.
    print('csv file ' + csv_file + ' written with quotes to ' + output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Commands for mapping script.')
    parser.add_argument('--csv_file', '-i',
                        help='The csv file')
    parser.add_argument('--output_file', '-o',
                        help='The output file')
    args = parser.parse_args()

    main(args.csv_file, args.output_file)
