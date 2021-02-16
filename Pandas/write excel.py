import xlsxwriter
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Bangla_word.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

for word in wordList:
    try:
        worksheet.write(row, col,     word)
        worksheet.write(row, col + 1, bl.lemma(word))
        row += 1
    except:
        worksheet.write(row, col,     word)
        worksheet.write(row, col + 1, DBSRA(word))
        row += 1     
          
workbook.close()
