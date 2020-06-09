import xlsxwriter


a = ["ddd", "334", "24dd", "det51"]

workbook = xlsxwriter.Workbook("demo3.xlsx")
worksheet = workbook.add_worksheet()

for i in range(len(a)):

    worksheet.write("A%d" % int(i+1), a[i])

workbook.close()
