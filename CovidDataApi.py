import requests
import json


class CovidData:

    def __init__(self, deaths, region, total_recovered, new_deaths, new_cases, serious_critical, active_cases,
                 total_cases_per_1m_population):
        self.deaths = deaths
        self.region = region
        self.total_recovered = total_recovered
        self.new_deaths = new_deaths
        self.new_cases = new_cases
        self.serious_critical = serious_critical
        self.active_cases = active_cases
        self.total_cases_per_1m_population = total_cases_per_1m_population


class MyAnalysisClass:

    def collect_data(self):

        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

        headers = {
            "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com",
            "X-RapidAPI-Key": "90165b2056msh5218e1ec6e762c2p1b30b0jsn0b7be9272e36"
        }

        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            parsed_data = json.loads(response.text)
            finalData = parsed_data['countries_stat']

            countryList = []

            for country in finalData:
                countryList.append(CovidData(country['deaths'], country['region'],
                                             country['total_recovered'], country['new_deaths'], country['new_cases'],
                                             country['serious_critical'], country['active_cases'], country['total_cases_per_1m_population']))
            return countryList

        else:
            print("Error: ")


covidData = MyAnalysisClass()
covidData.collect_data()
