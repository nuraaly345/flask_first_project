from openpyxl import Workbook

excel = Workbook()
page = excel.active
page['A1'] = 'Mouse'
page['A2'] = 'Keyboard'
page['A3'] = 'touchpad'
page['A4'] = 'microphon'
excel.save('task.xlsx')