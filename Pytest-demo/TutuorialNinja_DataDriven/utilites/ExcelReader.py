import openpyxl


def get_data(file_path: str, sheet_name: str) -> list:
   
    wb = openpyxl.load_workbook(file_path)
    ws = wb[sheet_name]

    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):  
      
        if all(cell is None for cell in row):
            continue

       
        cleaned = [str(cell).strip() if cell is not None else "" for cell in row]

        if len(cleaned) == 1:
          
            data.append(cleaned[0])
        else:
            data.append(tuple(cleaned))

    wb.close()
    return data