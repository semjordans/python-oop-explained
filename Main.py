import statistics


class District:
    def __init__(self, dictrictName, confirmedCases, hospitalised, deaths):
        self.dictrictName = dictrictName
        self.confirmedCases = confirmedCases
        self.hospitalised = hospitalised
        self.deaths = deaths

    def show_district_info(self):
        print(
            f"District name: {self.dictrictName} - Confirmed Cases: {self.confirmedCases} - Hospitalizations Cases: {self.hospitalised}"
            f" - Deaths Cases: {self.deaths}")


class COVID19Uganda:
    districts = []

    def add_district(self, district):
        self.districts.append(district)

    def show_district_details(self, searchName):
        for district in self.districts:
            if searchName != None:
                if searchName.lower() == district.dictrictName.lower():
                    return district.show_district_info()
                else:
                    district.show_district_info()  # print(f"No District called {searchName}")
            else:
                district.show_district_info()

    def confirmed_cases_count(self):
        confirmedCases = 0
        hospitalised = 0
        deaths = 0
        for district in self.districts:
            confirmedCases += int(district.confirmedCases)
            hospitalised += int(district.hospitalised)
            deaths += int(district.deaths)
        return District("SUMS", confirmedCases, hospitalised, deaths)

    def get_average(self):
        totals = len(self.districts)
        processedTotals = self.confirmed_cases_count()
        return District("Averages <> ", round(processedTotals.confirmedCases / totals, 0),
                        round(processedTotals.hospitalised / totals, 0),
                        round(processedTotals.deaths / totals, 0))
