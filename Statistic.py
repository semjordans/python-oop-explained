from Main import COVID19Uganda
from Main import District
import csv
from covid import Covid
import json
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objs as go

districts = []
cOVID19Uganda = COVID19Uganda()


def mainFun():
    print("Wecome to Jorda AI follow the menu ")
    print("-----------------------------------------")
    print("Enter (0) To Add a District")
    print("Enter (1) Import Districts from Covid Data to CSV")
    print("Enter (2) to Import Data From CSV")
    print("Enter (3) to get the Summations")
    print("Enter (4) to get Averages")
    print("Enter (5) to get Graphical Stats")
    print("Enter (6) To Search for a specific District")
    print("Enter (Q) to Exit")
    print("-----------------------------------------")

    while True:
        control = input("Enter Your Option Herer : ")
        if control == "Q":
            print("Thanks For using My Software")
            break
        else:
            if int(control) == 1:
                import_data_covid()
            elif int(control) == 0:
                proceed = True
                while proceed:
                    name = input("Enter District Name : ")
                    confirmed = int(input("Enter Confirmed Cases : "))
                    hospitalized = int(input("Enter Hospitalized Cases : "))
                    deaths = int(input("Enter Death Cases : "))
                    cOVID19Uganda.add_district(District(name, confirmed, hospitalized, deaths))

                    print(f"{name} : Has been added ")
                    addMore = int(input("Enter (1) or (0) to Proceed or Stop: "))

                    if addMore == 1:
                        proceed = True
                    else:
                        mainFun()
                        proceed = False


            elif int(control) == 2:
                import_from_csv()
            elif int(control) == 3:
                sumCoun = cOVID19Uganda.confirmed_cases_count()
                if sumCoun is not None:
                    print(
                        f"Case counts <> Confirmed Case: {sumCoun.confirmedCases} <> Hospitalised : {sumCoun.hospitalised} <> Deaths : {sumCoun.deaths}")
                else:
                    print("NOTE : Please add Some Districts Data to perform This Operation")

            elif int(control) == 4:
                averages = cOVID19Uganda.get_average()
                if averages is not None:
                    print(
                        f"Averages <> Confirmed Case: {averages.confirmedCases} <> Hospitalised : {averages.hospitalised} <> Deaths : {averages.deaths}")
                else:
                    print("NOTE : Please add Some Districts Data to perform This Operation")

            elif int(control) == 5:

                print("------------Welcome To Our Pretty Graphs---------")
                print("Enter (C) To Get Confirmed Cases Stats")
                print("Enter (H) To Get Hospitalised Cases")
                print("Enter (D) To Get Deaths Stats")
                print("************************************")
                print("Enter (Q) To Close Graphical Stats")

                myContinue = True
                while myContinue:
                    mySelect = input("Enter Your Option Here : ")
                    if mySelect.lower() == 'q':
                        myContinue = False
                        mainFun()
                    elif mySelect.lower() == 'c':
                        generate_stats_for_ten_test("Confirmed")
                    elif mySelect.lower() == 'h':
                        generate_stats_for_ten_test('Hospitalised')
                    elif mySelect.lower() == 'd':
                        generate_stats_for_ten_test('Deaths')
                    else:
                        print("Select Among the Provided Options")

            elif int(control) == 6:
                district = input("Enter District Name Or Enter Q to Quit: ")
                if district.lower() == "q":
                    mainFun()
                else:
                    cOVID19Uganda.show_district_details(district)


def generate_stats_for_ten_test(mySelect):
    # Show the plot
    plt.show()
    data = cOVID19Uganda.districts
    x = []
    y = []
    np.random.seed(3)
    plt.style.use('_mpl-gallery')

    for district in data[:5]:
        x.append(district.dictrictName)
        if mySelect == 'Confirmed':
            y.append(district.confirmedCases)
        elif mySelect == 'Hospitalised':
            y.append(district.hospitalised)
        elif mySelect == 'Deaths':
            y.append(district.deaths)

    plt.stem(x, y)

    # Add labels and title
    plt.xlabel('District')
    plt.ylabel('Numbers')
    plt.title('Districts Covid Stats')

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
        fieldnames = ['districtName', 'confirmed', 'active', 'deaths']
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
        pulledDistricts.append(
            {'districtName': districtName, 'confirmed': confirmed, 'active': active, 'deaths': deaths})

    return write_to_scv(pulledDistricts)


mainFun()
