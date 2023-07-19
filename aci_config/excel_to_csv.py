import pandas as pd
import sys

excelf_name = sys.argv[1]
excel_load = pd.ExcelFile(excelf_name)
sheetNames = excel_load.sheet_names
if "Info" in sheetNames:
	sheetNames.remove('Info')

for sheet_item in sheetNames:
	set_sheet = pd.read_excel(excelf_name, sheet_name=sheet_item, na_filter=False)
	if "mso" in excelf_name:
		set_sheet.to_csv(sheet_item+".csv", index=False)
#	if "mso" not in sheet_item:
#		print("No MSO: "+sheet_item)
#		set_sheet.to_csv(sheet_item+"-"+sys.argv[2]+".csv", index=False)
#	if "mso" in sheet_item:
#		if "staticport" or "tn_objects" in sheet_item:
#			print("MSO with StaticPort : "+sheet_item)
#			set_sheet.to_csv(sheet_item+"-"+sys.argv[2]+".csv", index=False)
	else:
#			print("MSO without StaticPort: "+sheet_item)
		set_sheet.to_csv(sheet_item+"-"+sys.argv[2]+".csv", index=False)
