__author__ = 'salmaelmalaki'

import csv
from subprocess import call
from matplotlib import pyplot


# Change ADB path based on your installation folder
ADB = 'C:/Users/Ari Berkowicz/AppData/Local/Android/Sdk/platform-tools/adb'


# Pull the power data from the phone
# data file is in the following form: time \t current \t voltage \t charge
call([ADB, 'pull', '/sdcard/Download/BatteryParameters/data'])


#################################################################
# Dictionaries and lists
time_vs_capacity_dict       =   dict()
time_vs_power_dict          =   dict()
time_vs_voltage_dict        =   dict()
time_vs_current_dict        =   dict()

time_lst                    =   list()
time_offsetfixed_lst        =   list()
capacity_lst                =   list()
power_lst                   =   list()
voltage_lst                 =   list()
current_lst                 =   list()
energy_lst                  =   list()
energy_lst.append(0) #initialize with 0
#################################################################
# Parse the power data file pulled from the phone
time = 0                # initialization
with open('data', 'rU') as data:
    for line in csv.reader(data, dialect="excel-tab"):
       # time     = float(line[0])
        current  = float(line[0])
        voltage  = float(line[1])
        capacity = float(line[2])

        power    = current * voltage

        time = time + 1         # each entry is at a new second
        # fill in the dictionaries and lists
        time_vs_capacity_dict[time] = capacity
        time_vs_current_dict[time]  = current
        time_vs_power_dict[time]    = power
        time_vs_voltage_dict[time]  = voltage

        time_lst.append(time)
        capacity_lst.append(capacity)
        power_lst.append(power)
        current_lst.append(current)
        voltage_lst.append(voltage)
        energy_lst.append(power + energy_lst[-1]) # integration of power

#################################################################
# Draw the traces
# Set the initial time to 0
initial_time = time_lst[0]
time_offsetfixed_lst[:] = [x - initial_time for x in time_lst]

pyplot.figure(0)
pyplot.title('change of capacity percentage')
pyplot.xlabel('time (hr)')
pyplot.plot(time_lst, capacity_lst, label='capacity')
pyplot.ylabel(' phone capacity (%)')
pyplot.legend(loc='upper right')
pyplot.savefig('time_vs_capacity.png')

pyplot.figure(1)
pyplot.title('change of power')
pyplot.xlabel('time (s)')
pyplot.plot(time_lst, power_lst, label='power')
pyplot.ylabel(' phone power')
pyplot.legend(loc='upper right')
pyplot.savefig('time_vs_power.png')


pyplot.figure(2)
pyplot.title('change of volt')
pyplot.xlabel('time (hr)')
pyplot.plot(time_lst, voltage_lst, label='volt')
pyplot.ylabel(' phone power')
pyplot.legend(loc='upper right')
pyplot.savefig('time_vs_volt.png')

del energy_lst[0] # delete the first element which was initialized to 0 at the beginning
pyplot.figure(3)
pyplot.title('change of energy')
pyplot.xlabel('time (hr)')
pyplot.plot(time_lst, energy_lst, label='energy')
pyplot.ylabel('consumed energy')
pyplot.legend(loc='upper right')
pyplot.savefig('time_vs_energy.png')
