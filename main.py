import statistics

class District:
  def __init__(self,  dictrictName, confirmedCases,hospitalizations,deaths):
    self.dictrictName = dictrictName
    self.confirmedCases = confirmedCases
    self.hospitalizations = hospitalizations
    self.deaths = deaths

  def show_district_info(self):
    print(f"District name: {self.dictrictName} - Confirmed Cases: {self.confirmedCases} - Hospitalizations Cases: {self.hospitalizations}"
          f" - Deaths Cases: {self.deaths}")


# district = District("Kampala", 20,30,1)
# district.show_district_info()

class COVID19Uganda:
    def __init__(self):
        self.districts = []

    def add_district(self, district):
        self.districts.append(district)

    def show_district_details(self):
        for district in self.districts:
            district.show_district_info()

    def confirmed_cases_count(self):
        confirmedCases = 0
        hospitalised = 0
        deaths = 0
        for district in self.districts:
            confirmedCases += district.confirmedCases
            hospitalised += district.hospitalizations
            deaths += district.deaths
        return print(f"Case counts <> Confirmed Case: {confirmedCases} Hospitalised : {hospitalised} Deaths : {deaths} ")

    def averages(self):
        confirmedCases = []
        hospitalised = []
        deaths = []
        for districtAv in self.districts:
            confirmedCases.append(districtAv.confirmedCases)
            hospitalised.append(districtAv.hospitalizations)
            deaths.append(districtAv.deaths)

        return print(f"Average <> Confirmed Case : { round(statistics.mean(confirmedCases),0)}  "
                     f"Hospitalised : {round(statistics.mean(hospitalised),0)}  "
                     f"Deaths : {round(statistics.mean(deaths),0)} ")

cOVID19Uganda = COVID19Uganda()

dis1 = District("Kampala",20,50,1)
dis2 = District("Wakiso",30,70,1)
dis3 = District("Mukono",10,30,1)

cOVID19Uganda.add_district(dis1)
cOVID19Uganda.add_district(dis2)
cOVID19Uganda.add_district(dis3)
# cOVID19Uganda.show_district_details()

cOVID19Uganda.show_district_details()
cOVID19Uganda.confirmed_cases_count()
cOVID19Uganda.averages()

# # print("All District Details:", cOVID19Uganda.show_district_details())
# print("Sumations:", cOVID19Uganda.confirmed_cases_count())
# print("Averages:", cOVID19Uganda.averages())