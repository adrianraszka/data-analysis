# TODO: ### Histogram wieku
import csv
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
import numpy as np

bins = [17, 24.3, 31.6, 38.9, 46.2, 53.5, 60.8, 68.1, 75.4, 82.7, 90]

with open('adultProba.csv', 'r') as excel:
    adults = list(csv.reader(excel))

    adults_age = []
    for row in adults:
        adults_age.append(row[1])
    adults_age.remove(adults_age[0])
    adults_age = list(map(int, adults_age))

    # Podział słupków w histogramie (od 10 co 10)
    # plt.hist(adults_age, bins=bins,
    #          color='g', edgecolor='black', linewidth=0.5)
    #
    # plt.ylabel('Ilość osób')
    # plt.xlabel('Wiek')
    #
    # plt.show()

# TODO: ###Histogram skategoryzowany
# import pandas as pd
# from matplotlib import pyplot as plt
# import numpy as np
# from matplotlib import style
#
# df = pd.read_csv('adultProba.csv')
# fig = plt.figure()

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
average = (sum(age_list) / (index + 1))  # 642 indexy, ale licząc od 0, więc 643 pomiary


age_list.sort()
# TODO: Odchylenie standardowe

suma = 0
liczba_el = len(age_list)
for i in range(len(age_list)):
    suma += ((age_list[i] - average) ** 2)
s = np.sqrt((suma / (liczba_el - 1)))
# print(s)

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
#
TODO: Wartość oczekiwana
# import pandas as pd
# from matplotlib import pyplot as plt
# import numpy as np
# from matplotlib import style
#
# df = pd.read_csv('adultProba.csv')
#
# # for index, row in df.iterrows():
# #     print(index, row['Age'])
#
# age_list = []
# for index, row in df.iterrows():
#     age_list.append(row['Age'])
# average = (sum(age_list) / (index + 1))  # 642 indexy, ale licząc od 0, więc 643 pomiary
#
# age_list.sort()
# # TODO: Odchylenie standardowe
#
# suma = 0
# liczba_el = len(age_list)
# for i in range(len(age_list)):
#     suma += ((age_list[i] - average) ** 2)
# s = np.sqrt((suma / (liczba_el - 1)))
# print(s)
#

TODO: Wykres gęstości
# import pandas as pd
# from matplotlib import pyplot as plt
# import numpy as np
# from matplotlib import style

# histogram = plt.hist(adults_age, bins=bins,
#                      color='g', edgecolor='black', linewidth=0.5, density=True)

# s - odchylenie standardowe, average - średnia

fx = []
for x in age_list:
    x = 1/(s * np.sqrt(2 * np.pi)) * np.exp( - (x - average)**2 / (2 * s ** 2))
    fx.append(x)

x_np = np.array(age_list)
fx_np = np.array(fx)

# plt.plot(x_np, fx_np, 'red')
# plt.show()
# #

# TODO: test 3 sigma
#
test_arr = []
for n in range(643):
    test_arr.append((n*100/643))

u3s, o3s = round(x_np.mean() - 3 * x_np.std(), 1), round(x_np.mean() + 3 * x_np.std(), 1)
u2s, o2s = round(x_np.mean() - 2 * x_np.std(), 1), round(x_np.mean() + 2 * x_np.std(), 1)
u1s, o1s = round(x_np.mean() - 1 * x_np.std(), 1), round(x_np.mean() + 1 * x_np.std(), 1)

print(u3s, o3s)
print(u2s, o2s)
print(u1s, o1s)
#
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
import math

perc = np.linspace(0,100,len(age_list))

# TODO: słupki na poszczególnych procentach
fig = plt.figure(1, (7,4))
ax1 = fig.add_subplot(1,1,1)
fmt = '%.0f%%'
xticks = mtick.FormatStrFormatter(fmt)
ax1.xaxis.set_major_formatter(xticks)
#
# ax2 = ax1.twinx()
# ax2.plot()

#
# # Pionowe linie
# fig = plt.figure(1, (7,4))
# ax1 = fig.add_subplot(1,1,1)
#
xcoords = [-3.2, 10.7, 24.7, 52.5, 66.5, 80.4]
colors = ['r', 'k', 'b', 'b', 'k', 'r']


for xc,c in zip(xcoords,colors):
    plt.axvline(x=xc, label='{}'.format(xc), c=c)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=6)

# plt.show()

x = np.linspace(average - 3*s, average + 3*s, 100)
plt.plot(x, stats.norm.pdf(x, average, s))
plt.show()
