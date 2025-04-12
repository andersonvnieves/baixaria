import openpyxl

def read(file_name, min_row, min_col, max_col) -> list:
    data = []
    wb = openpyxl.load_workbook(file_name)
    sheet = wb.active # ou active['<aba>']
    for row in sheet.iter_rows(min_row=min_row, min_col=min_col, max_col=max_col):
        data.append([ cell.value for cell in row ])

    return data
