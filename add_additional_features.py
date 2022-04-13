from openpyxl import load_workbook

wb = load_workbook('featuresv1.xlsx')
ws = wb['Sheet1']

with open('snr_values.txt') as f:
	snr = f.read()

with open('hnr_values.txt') as f:
	hnr = f.read()

snr = snr.split(',')

hnr = hnr.split(',')

counter = 1

for item in snr:
	index = 'CN' + str(counter) 
	ws[index] = 'snr_values'

	index2 = 'CN' + str(counter + 1)
	ws[index2] = item
	
	counter += 3

counter = 1

for item in hnr:
	index = 'CO' + str(counter)
	ws[index] = 'hnr_values'

	index2 = 'CO' + str(counter + 1)
	ws[index2] = item

	counter += 3

wb.save('featuresv1.xlsx')