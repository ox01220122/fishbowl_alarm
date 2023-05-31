import gspread

json_file_name = 'valid-progress-365508-34faab5e1cf8.json'
gc = gspread.service_account(filename=json_file_name)

    #리스트를 불러올
doc = gc.open_by_url("https://docs.google.com/spreadsheets/d/1YdADxUpk7Z70A697wOEZWOLMA-c8JJK5ug8lSJwyHDE/edit?usp=sharing")

worksheet=doc.worksheet("시트1")
tempList = worksheet.acell("A1").value
print(tempList)
worksheet.update_acell('A3', "4")
