
import json,csv

csvFilePath = "new_agent.csv"

 
#reading csv file and adding to json file..

data = {}
with open (csvFilePath) as  csvfile:
	csvReader = csv.DictReader(csvfile)
	for csvRow in csvReader:
		Date = csvRow['Name']
		data[Date] = csvRow


# now write to json file...

with open('json_data', 'w') as jsonFile:
	jsonFile.write(json.dumps(data,indent=4))