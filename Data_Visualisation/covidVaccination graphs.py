import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def line_vacc():
    # plot a graph.
    # vacc_drp.plot(x='date',y='total_vaccinations')
    plt.plot(vacc_drp['date'], vacc_drp['total_vaccinations'],c='orange', marker='.')
    plt.xlabel('Date of vaccination')
    plt.ylabel('Total vaccinations')
    plt.grid(True)
    plt.title(' Line Graph : Vaccinations and dates')
    plt.show()

def bar_vacc():
    # bar graph
    colors = ['orange', 'lightgreen', 'red','lightcoral']
    plt.bar(vacc_drp['date'], vacc_drp['total_vaccinations'],color = colors)
    plt.xlabel('Date of vaccination')
    plt.ylabel('Total vaccinations')
    plt.grid(True)
    plt.title('Line Graph :Vaccinations and dates')
    plt.show()

def scatter_vacc():
    # scatter graph
    plt.scatter(vacc_drp['date'], vacc_drp['total_vaccinations'],color = 'red',marker='.')
    plt.xlabel('Date of vaccination')
    plt.ylabel('Total vaccinations')
    plt.grid(True)
    plt.title('Scatter graph - Vaccinations and dates')
    plt.show()


# ********************* main program ***********************

vacc = pd.read_csv('India.csv')

# print(vacc.head())
# print(vacc.info())
# print(vacc.shape)

# fill the missing values
vacc_drp = vacc.fillna(value={'total_boosters': 0})

# Check for missing values
vacc_drp = vacc_drp.dropna()

# remove the duplicates.
vacc_drp = vacc_drp.drop_duplicates()

# Convert to datetime
vacc_drp['date'] = pd.to_datetime(vacc_drp['date'])

# Convert to numeric
vacc_drp['total_vaccinations'] = pd.to_numeric(vacc_drp['total_vaccinations'])

# print(vacc_drp['total_vaccinations'])
# print(" now here")

while(1):
    ch = input("Enter your choice : \n 1. line graph\n 2. bar graph \n 3. scatter graph \n 4. exit \n")
    if ch == '1':
        line_vacc()
    elif ch == '2':
        bar_vacc()
    elif ch == '3':
        scatter_vacc()
    else:
        break




