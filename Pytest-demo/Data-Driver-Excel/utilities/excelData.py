import openpyxl
import os


def get_data(file_name, sheet_name):
    base_dir  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, "Excelfiles", file_name)

    workbook = openpyxl.load_workbook(full_path)
    sheet    = workbook[sheet_name]

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if any(cell is not None for cell in row):
            data.append(row)

    return data
