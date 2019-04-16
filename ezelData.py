#TODO: ### Histogram wieku
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


# TODO: ###Histogram skategoryzowany
# import pandas as pd
# from matplotlib import pyplot as plt
# import numpy as np
# from matplotlib import style
#
# df = pd.read_csv('adultProba.csv')
#
#
# fig = plt.figure()
#
#
#
#
# male_u50 = []
# male_o50 = []
# female_u50 = []
# female_o50 = []
# for index, row in df.iterrows():
#     #male under 50k
#     if row['sex'] == 'Male' and row['Income'] == '<=50K':
#         male_u50.append(row['Age'])
#     #male over 50k
#     elif row['sex'] == 'Male' and row['Income'] == '>50K':
#         male_o50.append(row['Age'])
#
#     # female under 50k
#     elif row['sex'] == 'Female' and row['Income'] == '<=50K':
#         female_u50.append(row['Age'])
#
#     # female over 50k
#     elif row['sex'] == 'Female' and row['Income'] == '>50K':
#         female_o50.append(row['Age'])
#
#
# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)
#
# ax1.hist(male_u50, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90],
#              color='r', edgecolor='black', linewidth=0.5)
# ax2.hist(male_o50, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90],
#              color='g', edgecolor='black', linewidth=0.5)
# ax3.hist(female_u50, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90],
#              color='b', edgecolor='black', linewidth=0.5)
# ax4.hist(female_o50, bins=[10, 20, 30, 40, 50, 60, 70, 80, 90],
#              color='k', edgecolor='black', linewidth=0.5)
#
# a,b = 0,100
#
# ax1.set_xlabel('Wiek')
# ax1.set_ylabel('Ilość osób')
# ax1.set_title('Mężczyźni zarabiający powyżej 50 000')
# ax1.set_ylim(a,b)
#
# ax2.set_xlabel('Wiek')
# ax2.set_ylabel('Ilość osób')
# ax2.set_title('Mężczyźni zarabiający poniżej 50 000')
# ax2.set_ylim(a,b)
#
# ax3.set_xlabel('Wiek')
# ax3.set_ylabel('Ilość osób')
# ax3.set_title('Kobiety zarabiający powyżej 50 000')
# ax3.set_ylim(a,b)
#
# ax4.set_xlabel('Wiek')
# ax4.set_ylabel('Ilość osób')
# ax4.set_title('Kobiety zarabiający poniżej 50 000')
# ax4.set_ylim(a,b)
#
# plt.tight_layout()
# plt.show()

# TODO: Wartość oczekiwana
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import style

df = pd.read_csv('adultProba.csv')

# for index, row in df.iterrows():
#     print(index, row['Age'])

age_list = []
for index, row in df.iterrows():
    age_list.append(row['Age'])
average = (sum(age_list)/(index + 1)) #642 indexy, ale licząc od 0, więc 643 pomiary

# TODO: Odchylenie standardowe

suma = 0
liczba_el = len(age_list)
for i in range(len(age_list)):
    suma += ((age_list[i] - average)**2)
s = np.sqrt((suma/(liczba_el-1)))
print(s)
# s += ((sum(age_list[i] - average)**2))
    # print(s)