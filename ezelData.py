### Histogram wieku
# import csv
# import pandas as pd
# from scipy import stats
# from matplotlib import pyplot as plt
# import numpy as np
#
# with open('adultProba.csv', 'r') as excel:
#     adults = list(csv.reader(excel))
#
#     adults_age = []
#     for row in adults:
#         adults_age.append(row[1])
#     adults_age.remove(adults_age[0])
#     adults_age = list(map(int, adults_age))
#
#     #Podział słupków w histogramie (od 10 co 10)
#     plt.hist(adults_age, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90],
# #              color='g', edgecolor='black', linewidth=0.5)
# #
# #     plt.ylabel('Ilość osób')
# #     plt.xlabel('Wiek')
#
#     plt.show()

# import matplotlib.pyplot as plt
#
# apl_price = [93.95, 112.15, 104.05, 144.85, 169.49]
# ms_price = [39.01, 50.29, 57.05, 69.98, 94.39]
# year = [2014, 2015, 2016, 2017, 2018]
#
# plt.plot(year, apl_price,
#          year, ms_price)
# plt.xlabel('Year')
# plt.ylabel('Stock Price')
# plt.show()


###Histogram skategoryzowany
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df = pd.read_csv('adultProba.csv')
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()




male_u50 = []
male_o50 = []
female_u50 = []
female_o50 = []
for index, row in df.iterrows():
    #male under 50k
    if row['sex'] == 'Male' and row['Income'] == '<=50K':
        male_u50.append(row['Age'])
    #male over 50k
    elif row['sex'] == 'Male' and row['Income'] == '>50K':
        male_o50.append(row['Age'])

    # female under 50k
    elif row['sex'] == 'Female' and row['Income'] == '<=50K':
        female_u50.append(row['Age'])

    # female over 50k
    elif row['sex'] == 'Female' and row['Income'] == '>50K':
        female_o50.append(row['Age'])


ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.hist(male_u50, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90],
             color='r', edgecolor='black', linewidth=0.5)
ax2.hist(male_o50, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90],
             color='g', edgecolor='black', linewidth=0.5)
ax3.hist(female_u50, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90],
             color='b', edgecolor='black', linewidth=0.5)
ax4.hist(female_o50, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90],
             color='k', edgecolor='black', linewidth=0.5)

ax1.ylabel('Ilość osób')
ax1.xlabel('Wiek')
ax1.title('Male')
ax1.subtitle('Rozkład wieku przy dochodach poniniżej 50K')

ax2.ylabel('Ilość osób')
ax2.xlabel('Wiek')
ax2.title('Male')
ax2.subtitle('Rozkład wieku przy dochodach powyżej 50K')

ax3.ylabel('Ilość osób')
ax3.xlabel('Wiek')
ax3.title('Female')
ax3.subtitle('Rozkład wieku przy dochodach poniniżej 50K')

ax4.ylabel('Ilość osób')
ax4.xlabel('Wiek')
ax4.title('Female')
ax4.subtitle('Rozkład wieku przy dochodach powyżej 50K')

plt.show()

# income_list = []
# for row in df['Income']:
#     income_list.append(row)
# print(set(income_list))

# plt.ylabel('Usage')
# plt.title('Programming language usage')
#
# plt.show()