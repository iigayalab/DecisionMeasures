import numpy
import pandas
import rdata

dallTrain = pandas.read_csv('/Users/anusha/Downloads/DallTrain.csv')
dallTest = pandas.read_csv('/Users/anusha/Downloads/DallTest.csv')

combinedData = dallTrain.append(dallTest, ignore_index=True)
column_names = combinedData.columns
combinedData["nspnID"] = pandas.NaT

parsed = rdata.parser.parse_file("/Users/anusha/Downloads/AllD18.RData")
converted = rdata.conversion.convert(parsed)
alldata = converted['AllD18']
alldata = alldata.reset_index()

for i in range(len(combinedData)):
    for j in range(len(alldata)):
        num_of_na = 0
        num_matched = 0
        for column in column_names:
            if pandas.isna(alldata.loc[j, column]) and pandas.notna(combinedData.loc[i, column]):
                num_of_na = num_of_na + 1
            elif round(alldata.loc[j, column], 6) != round(combinedData.loc[i, column], 6):
                break
            else:
                num_matched = num_matched + 1
        if (num_matched+num_of_na) == 31 and num_matched > 15:
            combinedData.loc[i, 'nspnID'] = alldata.loc[j, 'nspnID']
            break

combinedData.to_csv('/Users/anusha/Downloads/combinedData_with_IDs.csv', index=False)
