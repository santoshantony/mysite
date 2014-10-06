# import a excel file and print
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

pd.set_option('expand_frame_repr', False)
# setting up data
# datatype = ['vat_no': S11,'amount': i5]
bd = pd.read_csv('/home/santosh/Documents/b_sup_data.csv')
hd = pd.read_csv('/home/santosh/Documents/h_sup_data.csv')

os.system('clear')

raw_input('setting up data from HeadOffice and BranchOffice...')

hd.set_index('no', inplace=True)
print hd
print '@Head Office'
print 'Monthly Sales in INR :',  hd['amount'].sum(), 'Vat Tax Total:', hd['tax'].sum()
# print hd.dtypes

bd.set_index('no', inplace=True)
print bd
print '@Branch Office'
print 'Monthly Sales in INR :',  bd['amount'].sum(), 'Vat Tax Total:', bd['tax'].sum()

raw_input('Above is HeadOffice and Branch Office Data.Press any key to continue....')
# Consolidating Data
cd = hd.append(bd)

raw_input('\nConsolidatng data.. \n')
print cd
print 'Consolidated figures of Head Ofice and Branch Office'
print 'Monthly Sales in INR :',  cd['amount'].sum(), 'Vat Tax Total:', cd['tax'].sum()

# Generating Data for upload...
writer = pd.ExcelWriter('vat.xlsx', engine='xlsxwriter')
cd.to_excel(writer, sheet_name='sheet1')
writer.save()

# To do List
# Adding row totals to selected coloumns
# Data validation
# Yaml for preparing a configuration file
print('The End')
