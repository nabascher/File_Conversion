#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      jsmit
#
# Created:     24/03/2021
# Copyright:   (c) jsmit 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
if __name__ == '__main__':
    main()
import os
import pandas as pd
directory = os.getcwd()
folders = ['norpix','xmlcombo','flagger']
for i in folders:
    files = os.listdir(directory + '/' + i)
    csv_total = pd.DataFrame()
    excel_total = pd.DataFrame()
    for file in files:
        if file.endswith('.csv'):
            csv_file = pd.read_csv(directory + '\\' + i + '\\' + file)
            csv_total = csv_total.append(csv_file)
            csv_total.to_csv(directory + '/' + i + '_europa' + '.csv')
        elif file.endswith('.xlsx'):
            excel_file = pd.read_excel(directory + '\\' + i + '\\' + file)
            excel_total = excel_total.append(excel_file)
            excel_total.to_excel(directory + '/' + i + '_europa' + '.xlsx')
