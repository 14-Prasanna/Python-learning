import openpyxl

def get_data(path, sheet):
    final_list =[]

    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet]
    total_row = sheet.max_row
    total_col = sheet.max_column

    for r in range(2, total_row+1):
        row_kist = []

        for c in range(1, total_col+1):
            row_kist.append(sheet.cell(r,c).value)

        final_list.append(row_kist)

    
    return final_list
