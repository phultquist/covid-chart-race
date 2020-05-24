#note: the missing get_data() function is found in the main script

def get_country_population(country):
    tmp = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=world-population%%40kapsarc&q=%s&sort=year&facet=year&facet=country_name"
    cmd = tmp % (country)
    res = requests.get(cmd)
    dct = json.loads(res.content)
    try:
        out = dct['records'][0]['fields']['value']
    except:
        print(country+" does not have population data")
        return -1
    return out

def write_pops(pops, da):
    fin = []
    for i in range(len(pops)):
        if pops[i]==-1:
            x=1
        else:
            da[i][0] = pops[i]
            fin.append(da[i])

    write_data(fin)


base_data = get_data()

def get_all_pops(da):
    populations = []
    for i in range(0,len(da)):
        name = da[i][1]
        # print(name)
        pop = get_country_population(name)
        populations.append(pop)
        print(name + ": " + str(pop))

    return populations

def write_data(new_data):
    joinstr = ","
    for i in range(len(new_data)):
        new_data[i] = list(map(str, new_data[i]))
        new_data[i] = joinstr.join(new_data[i])

    joinstr = '\n'
    final_str = joinstr.join(new_data)
    # print(final_str)

    file = open("cases.csv",mode="w")
    file.write(final_str)
    file.close()

write_pops(get_all_pops(base_data), base_data)
