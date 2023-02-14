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
        print(searchName)
        for district in self.districts:
            if searchName != None:
                if searchName.casefold() == district.dictrictName.casefold():
                    return district.show_district_info()
                # print(f"No District called {searchName}")
            else:
                district.show_district_info()

    def confirmed_cases_count(self):
        if len(self.districts) > 0:
            confirmedCases = 0
            hospitalised = 0
            deaths = 0
            for district in self.districts:
                confirmedCases += int(district.confirmedCases)
                hospitalised += int(district.hospitalised)
                deaths += int(district.deaths)
            return District("SUMS", confirmedCases, hospitalised, deaths)
        else:
            print(f"Please Add Some districts To Curry out this Operation")

    def get_average(self):
        if len(self.districts) > 0:
            totals = len(self.districts)
            processedTotals = self.confirmed_cases_count()
            return District("Averages <> ", round(processedTotals.confirmedCases / totals, 0),
                            round(processedTotals.hospitalised / totals, 0),
                            round(processedTotals.deaths / totals, 0))

        else:
            District("Averages <> ", 0, 0, 0)
