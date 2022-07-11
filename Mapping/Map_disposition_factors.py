import pandas
import numpy

sym_file_data = pandas.read_csv('/Users/anusha/Downloads/symfacdeciq.csv')
req_columns = sym_file_data.columns

dec_fac_data = pandas.read_csv('/Users/anusha/Downloads/combinedData_with_IDs.csv')

for col in req_columns:
    if col != 'nspnID':
        dec_fac_data[col] = numpy.nan

for index in range(len(dec_fac_data)):
    for sym_index in range(len(sym_file_data)):
        if sym_file_data.loc[sym_index, 'nspnID'] == dec_fac_data.loc[index, 'nspnID']:
            for col in req_columns:
                dec_fac_data.loc[index, col] = sym_file_data.loc[sym_index, col]
            break

dec_fac_data.to_csv('/Users/anusha/Downloads/combined_dataset_all.csv')
