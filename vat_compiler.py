# import a excel file and print
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

pd.set_option('expand_frame_repr', False)
# setting up data
# datatype = ['vat_no': S11,'amount': i5]
# data = ('')

# bd = pd.read_csv('/home/santosh/Documents/b_sup_data.csv')
# hd = pd.read_csv('/home/santosh/Documents/h_sup_data.csv')


bd = pd.read_csv('/home/santosh/Documents/aug_anx1_bo.csv')
hd = pd.read_csv('/home/santosh/Documents/aug_anx1_ho.csv')

os.system('clear')

raw_input('setting up data from HeadOffice and BranchOffice...')

hd.set_index('serial_no', inplace=True)
print hd
print '@Head Office'
print 'Monthly Sales in INR :',  hd['Purchase_Value'].sum(), 'Vat Tax Total:', hd['VAT_CST_paid'].sum()
print 'No of rows:', hd.count()
# print hd.dtypes

bd.set_index('serial_no', inplace=True)
print bd
print '@Branch Office'
print 'Monthly Sales in INR :',  bd['Purchase_Value'].sum(), 'Vat Tax Total:', bd['VAT_CST_paid'].sum()
print 'No of rows:', bd.count()

raw_input('Above is HeadOffice and Branch Office Data.Press any key to continue....')
# Consolidating Data
cd = hd.append(bd)

raw_input('\nConsolidatng data.. \n')
print cd
print 'Consolidated figures of Head Ofice and Branch Office'
print 'Monthly Sales in INR :',  cd['Purchase_Value'].sum(), 'Vat Tax Total:', cd['VAT_CST_paid'].sum()
print 'No of rows:', cd.count()
# Group by vat rate
raw_input('Grouping the data according to vat_rate')
os.system('clear')
gbcd = cd.sort('Tax_rate')
print gbcd

# Generating Data for upload...
writer = pd.ExcelWriter('vat.xlsx', engine='xlsxwriter')
cd.to_excel(writer, sheet_name='sheet1')
writer.save()

# To do List
# Adding row totals to selected coloumns
# Data validation
# Yaml for preparing a configuration file
print('The End')
