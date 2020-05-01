# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print(data.shape)
census = np.concatenate([data,new_record])
#print(census)

age=census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

race = census[:,2]
race_0 = race[race == 0 ]
race_1 = race[race==1]
race_2 = race[race==2]
race_3 = race[race==3]
race_4 = race[race == 4]
len_0 = len(race_0)

len_1 = len(race_1)

len_2 = len(race_2)

len_3 = len(race_3)

len_4 = len(race_4)

minority_race = np.min([len_0,len_1,len_2,len_3,len_4])/2
print(minority_race)

age1 = age[age>60]
senior_citizens=census[census[:,0]>60]
working_hours_sum =  np.sum(senior_citizens[:,6])
print(working_hours_sum)

avg_working_hours = np.round(np.average(senior_citizens[:,6]),2)
print(avg_working_hours)

high = census[census[:,1]>10]
low = census[census[:,1]<10]

avg_pay_high = np.round(np.average(high[:,7]),2)
print(avg_pay_high)
avg_pay_low = np.round(np.average(low[:,7])+0.01,2)
print(avg_pay_low)


