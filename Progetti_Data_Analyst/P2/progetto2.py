import csv
t_italy_cases = []
t_germany_cases = []
t_italy_deaths = []
t_germany_deaths = []
t_europe_prate = []
t_asia_prate = []
with open("C:\\Users\\Kai_J\\Desktop\\Data_Analyst\\Progetti_Data_Analyst\\P2\\owid-covid-data.csv", "r") as csv_file:
    dataset = csv.reader(csv_file)
    
    for i in dataset:           # Morti e casi Covid19 in Italia e Germania
        if i[3] == 'Italy' and i[5] != "":
             t_italy_cases.append(float(i[5]))
        elif i[3] == 'Germany' and i[5] != "":
             t_germany_cases.append(float(i[5]))
        if i[3] == 'Italy' and i[8] != "":
            t_italy_deaths.append(float(i[8]))
        elif i[3] == 'Germany' and i[8] != "":
            t_italy_deaths.append(float(i[8]))
        if i[2] == 'Europe' and i[29] != "":            #Tasso di positivita' fra Europa e Asia
             t_europe_prate.append(float(i[29]))
        elif i[2] == 'Asia' and i[29] != "":
             t_asia_prate.append(float(i[29]))


        def average(a, b):           #Media casi totali
            return (a + b) / 2
        avg1 = average(float(t_italy_cases[-1]), float(t_germany_cases[-1]))
        print("Casi totali in Italia: ", t_italy_cases[-1])
        print("Casi totali in Germania: ", t_germany_cases[-1])
        print("La media dei casi totali fra Italia e Germania corrisponde a: ", avg1)


        def average(a, b):           #Media morti totali
            return (a + b) / 2
        avg2 = average(float(t_italy_deaths[-1]), float(t_germany_deaths[-1]))
        print("Morti totali in Italia: ", t_italy_deaths[-1])
        print("Morti totali in Germania: ", t_germany_deaths[-1])
        print("La media delle morti totali fra Italia e Germania corrisponde a: ", avg2)


        def average(a, b):           #Media tasso di positivita'
            return (a + b) / 2
        avg3 = average(float(t_europe_prate[-1]), float(t_asia_prate[-1]))
        print("Tasso di positivita' in Europa: ", t_europe_prate[-1])
        print("Tasso di positivita' in Asia: ", t_asia_prate[-1])
        print("La media del tasso di positivita' fra Europa e Asia corrisponde a: ", avg3)