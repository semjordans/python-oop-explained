from Main import COVID19Uganda
from Main import District
import csv
from covid import Covid
import json
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

districts =[]
cOVID19Uganda = COVID19Uganda()
def mainFun():
    print("Wecome to Jorda AI follow the menu ")
    print()
    print("Enter (1) Import Districts from Covid Data to CSV")
    print("Enter (2) to Import Data From CSV")

    # if(len(cOVID19Uganda.districts)>0):
    print("Enter (3) to get the Summations")
    print("Enter (4) to get Averages")
    print("Enter (5) to get Graphical Stats")
    print("Eneter 5 to Exit")
    # else:
    # print("##### --- Import Data To get More Options --- #####")



    while True:
        control = input()
        if control == "Q":
            print("Thanks For using My Software")
            break
        else:
            if int(control) == 1:
                import_data_covid()
            elif int(control) == 2:
                import_from_csv()
            elif int(control) == 3:
                sumCoun =   cOVID19Uganda.confirmed_cases_count()
                print(f"Case counts <> Confirmed Case: {sumCoun.confirmedCases} <> Hospitalised : {sumCoun.hospitalised} <> Deaths : {sumCoun.deaths}")
            elif int(control) == 4:
                averages = cOVID19Uganda.averageModifed()
                print(f"Averages <> Confirmed Case: {averages.confirmedCases} <> Hospitalised : {averages.hospitalised} <> Deaths : {averages.deaths}")
            elif int(control) == 5:
                generate_stats_for_ten_plot()


def generate_stats_for_ten():

    data = cOVID19Uganda.districts
    x = []
    y = []

    for district in data[:5]:
        x.append(district.dictrictName)
        y.append(district.deaths)
    plt.scatter(x, y)

    plt.title("To 5 Districts")
    plt.xlabel("District")
    plt.ylabel("Deaths")

    plt.show()

def generate_stats_for_ten_plot():

    data = cOVID19Uganda.districts
    A = []
    B = []

    for district in data[:5]:
        A.append(district.dictrictName)
        B.append(district.deaths)

    df = pd.DataFrame({'x': A, 'y': B})

    fig = px.line(df, x='x', y='y')

    fig.show()



def import_from_csv():
    with open('myData.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dis1 = District(row['districtName'], row['confirmed'], row['active'], row['deaths'])
            cOVID19Uganda.add_district(dis1)
    return print(f" {len(cOVID19Uganda.districts)} <> Districts Have Been Imported from CSV")


def write_to_scv(data):
    fileName = "myData.csv"
    # print(data)
    with open(fileName, 'w', newline='') as csvfile:
        fieldnames = ['districtName', 'confirmed', 'active','deaths']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)
    return print(f"{len(data)}Districts Have Been Add To the CSV file")

def import_data_covid():
    covid = Covid()
    covidData = covid.get_data()
    json_data = json.dumps(covidData, indent=4)
    data = json.loads(json_data)
    pulledDistricts = []

    for item in data:
        districtName = item['country']
        confirmed = item['confirmed']
        active = item['deaths']
        deaths = item['deaths']
        pulledDistricts.append({'districtName': districtName, 'confirmed': confirmed, 'active': active, 'deaths': deaths})

    return write_to_scv(pulledDistricts)

mainFun()
