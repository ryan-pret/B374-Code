import openpyxl
from pathlib import Path
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import math
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# wb_obj = openpyxl.load_workbook('owid-covid-data.xlsx')
wb_obj = openpyxl.load_workbook('C:/Users/preto/Desktop/B374-Code/stats/owid-covid-data.xlsx') 

# Read the active sheet:
sheet = wb_obj.active

rows = sheet.rows

headers = [cell.value for cell in next(rows)]

list_dict = []

# Afghanistan
## Get data
for row in rows:
    data = {}
    flag = False
    for title, cell in zip(headers, row):
        if cell.value == "South Sudan":
            flag = True

        if flag and title == "new_cases":
            data[title] = cell.value

        if flag and title == "date":
            data[title] = cell.value

    # for title, cell in zip(headers, row):
        # print(title, cell.value)
        # if cell.value == "AFG":
        #     data[title] = cell.value
    list_dict.append(data)
    # filter(None, data)
# print(list_dict)

dates = []
y = []
for dic in list_dict:
    for key in dic:
        if key == 'date':
            dates.append(dic[key])
        if key == 'new_cases':
            if dic[key] != None:
                y.append(dic[key])
        # print(key)
        # print(dic[key])
    # if dat['date'] != None:
    #     dates.append(dat['date'])
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]

bins = math.ceil(1 + math.log2(len(y)))
legend = ['new cases daily']

new_y = np.array(y)
print(new_y)

# Creating histogram
fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7),
                        tight_layout = True)
 
axs.hist(new_y, bins = bins)

plt.xlabel("Range of recorded new daily cases")
plt.ylabel("Number of cases in interval")
plt.title('Histogram of new Covid-19 cases recorded in South Sudan')
plt.legend(legend)
plt.show()