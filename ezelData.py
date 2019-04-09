import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


with open('adultProba.csv', 'r') as excel:
    adults = list(csv.reader(excel))

    adults_age = []
    for row in adults:
        adults_age.append(row[1])
    adults_age.remove(adults_age[0])
    adults_age = list(map(int, adults_age))

plt.hist(adults_age, bins=range(min(adults_age), max(adults_age))
plt.ylabel('No of times')
plt.show()

# Titles = []
# IDs = []
# Age = []
# Work_class = []
# fnlwgt = []
# education = []
# education_num = []
# martial_status = []
# occupation = []
# relationship = []
# race = []
# sex = []
# capital_gain = []
# capital_loss = []
# hours_per_week = []
# native_country = []
# income = []

        # ID = [0]
        # IDs.append(IDs)
        # Age.append(Age)
        # Work_class.append(Work_class)
        # fnlwgt.append(fnlwgt)
        # education.append(education)
        # education_num.append(education_num)
        # martial_status.append(martial_status)
        # occupation.append(occupation)
        # relationship.append(relationship)
        # race.append(race)
        # sex.append(sex)
        # capital_gain.append(capital_gain)
        # capital_loss.append(capital_loss)
        # hours_per_week.append(hours_per_week)
        # native_country.append(native_country)
        # income.append(income)



















