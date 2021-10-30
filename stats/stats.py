import openpyxl
from pathlib import Path
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

# wb_obj = openpyxl.load_workbook('owid-covid-data.xlsx')
wb_obj = openpyxl.load_workbook('C:/Users/preto/Desktop/B374/stats/owid-covid-data.xlsx') 

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

        if flag and title == "total_vaccinations":
            data[title] = cell.value

        if flag and title == "date":
            data[title] = cell.value

    # for title, cell in zip(headers, row):
        # print(title, cell.value)
        # if cell.value == "AFG":
        #     data[title] = cell.value
    list_dict.append(data)
    # filter(None, data)
print(list_dict)

dates = []
y = []
for dic in list_dict:
    for key in dic:
        if key == 'date':
            dates.append(dic[key])
        if key == 'total_vaccinations':
            y.append(dic[key])
        # print(key)
        # print(dic[key])
    # if dat['date'] != None:
    #     dates.append(dat['date'])

print(dates)
# dates = ['01-02-1991','01-03-1991','01-04-1991']
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates]
# y = range(len(x)) # many thanks to Kyss Tao for setting me straight here
 
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator())
# plt.plot(x,y)
# plt.gcf().autofmt_xdate()

plt.plot(x, y)
 
# naming the x axis
plt.xlabel('Dates')
# naming the y axis
plt.ylabel('Number of vaccine dosages administered')
 
# giving a title to my graph
plt.title('Covid-19 total vaccination dosages administered over time in South Sudan')
 
# function to show the plot
plt.show()

# plt.show()