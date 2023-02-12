from CovidDataApi import CovidData
from CovidDataApi import MyAnalysisClass
from prettytable import PrettyTable

# covidData = CovidData()
myAnalysisClass = MyAnalysisClass()


def mainFunc():
    print("Welcome To The World Covid Data Analysis ")
    print("-----------------------------------------")
    print("Enter (1) To Display Data From Covid Open API")
    print("Enter (2) To Import Covid Data to CSV File")
    print("Enter (Q or Quit) To Close the Application")
    print("-----------------------------------------")

    while True:
        control = input("Enter Your Option Herer : ")
        if control.lower() == 'q' or control.lower() == "quit":
            print("Thanks For using My Software")
            break
        else:
            if int(control) == 1:
                print(">>>>> Below is the Data you have requested for <<<<<< ")
                construct_data_for_display()
            elif int(control) == 2:
                myAnalysisClass.export_to_csv()


def construct_data_for_display():
    myData = myAnalysisClass.collect_data()

    table = PrettyTable()
    table.field_names = ['Country', 'Deaths', 'Region', 'Recovered', 'New Deaths', 'New Cases',
                         'Critical', 'Active Cases', 'Cases per 1M ']

    for country in myData:
        table.add_row(
            [country.country_name, country.deaths, country.region, country.total_recovered, country.new_deaths,
             country.new_cases, country.serious_critical, country.active_cases, country.total_cases_per_1m_population])

    return print(table)


mainFunc()
