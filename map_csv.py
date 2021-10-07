'''
This script takes two csv files, then maps specific columns of the CSV files using rows or columns.

Input:
########
    * -a, --csv_file1 : CSV file to map
    * -b, -csv_file2 : CSV file to use for mapping
    * -m, -map_by : user specified command to map by rows or columns
    * -t, --transpose : user specified command to switch rows to columns and vice versa

Output:
########
    * -o, --output_file : path and file name of the mapped CSV file

Usage:
########
    * python quote_csv.py -h

        * Gives a description of the commands

    * python quote_csv.py -a <path/csv1_filename.csv> -b <path/csv2_filename.csv> -m <rows/columns> -t <yes/no>

        * Runs the script with the given commands
'''

import pandas as pd
import argparse

def main(csv_file1, csv_file2, map_by, transpose, output_file):
    '''
    Perform the mapping function given the input CSV files and user commands for map by and transpose.

    Write to a new CSV file.
    '''

    # Load both csv files into pandas dataframes
    csv1_df = pd.read_csv(csv_file1)
    print(csv1_df)

    csv2_df = pd.read_csv(csv_file2)
    print(csv2_df)

    # Check to see if mapping should occur by column or rows
    if 'columns' in map_by:
        final_df = pd.concat([csv1_df, csv2_df], sort=False, ignore_index=True)

    elif 'rows' in map_by:
        print('Function not built yet.')
        # full_df = pd.merge(left=csv_file1, right=csv_file2, how='outer', left_on='id', right_on='id')

    else:
        print('Must enter "columns" or "rows" for map_by variable')
        exit()

    # Check to see if the final table should be transposed (columns and rows switch)
    if 'yes' in transpose:
        print('Transposing columns and rows in final table')
        final_df = final_df.transpose()
        final_df.columns = ['csv1_value', 'csv2_value']


    elif 'no' in transpose:
        print('Script will NOT transpose columns and rows in final table')

    else:
        print('Choose a transpose option "yes" or "no". Transpose will make all columns into rows and all rows into columns.')
        exit()

    print('Writing dataframe to ' + output_file)

    final_df.to_csv(output_file, index=True)


# Command line arguments.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Commands for mapping script.')
    parser.add_argument('--csv_file1', '-a',
                        help='csv file 1')
    parser.add_argument('--csv_file2', '-b',
                        help='csv file 2')
    parser.add_argument('--map_by', '-m',
                        help='map_by option choice')
    parser.add_argument('--transpose', '-t',
                        help='transpose option choice')
    parser.add_argument('--output_file', '-o',
                        help='The output file')
    args = parser.parse_args()

    main(args.csv_file1, args.csv_file2, args.map_by, args.transpose, args.output_file)
