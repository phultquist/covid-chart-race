from graphics import *
import requests
import json
import random

(w,h) = (800,400)

data_start = 4

population_minimum = 1000000
num_countries_in_graph = 20

header = 'Population,Country/Region,Lat,Long,1/22/20,1/23/20,1/24/20,1/25/20,1/26/20,1/27/20,1/28/20,1/29/20,1/30/20,1/31/20,2/1/20,2/2/20,2/3/20,2/4/20,2/5/20,2/6/20,2/7/20,2/8/20,2/9/20,2/10/20,2/11/20,2/12/20,2/13/20,2/14/20,2/15/20,2/16/20,2/17/20,2/18/20,2/19/20,2/20/20,2/21/20,2/22/20,2/23/20,2/24/20,2/25/20,2/26/20,2/27/20,2/28/20,2/29/20,3/1/20,3/2/20,3/3/20,3/4/20,3/5/20,3/6/20,3/7/20,3/8/20,3/9/20,3/10/20,3/11/20,3/12/20,3/13/20,3/14/20,3/15/20,3/16/20,3/17/20,3/18/20,3/19/20,3/20/20,3/21/20,3/22/20,3/23/20,3/24/20,3/25/20,3/26/20,3/27/20,3/28/20,3/29/20,3/30/20,3/31/20,4/1/20,4/2/20,4/3/20,4/4/20,4/5/20,4/6/20,4/7/20,4/8/20,4/9/20,4/10/20,4/11/20,4/12/20,4/13/20,4/14/20,4/15/20,4/16/20,4/17/20,4/18/20,4/19/20,4/20/20,4/21/20,4/22/20,4/23/20,4/24/20,4/25/20,4/26/20,4/27/20,4/28/20,4/29/20,4/30/20,5/1/20,5/2/20,5/3/20,5/4/20,5/5/20,5/6/20,5/7/20,5/8/20,5/9/20,5/10/20,5/11/20,5/12/20,5/13/20,5/14/20,5/15/20,5/16/20'

dates = header.split(",")[data_start:]

def get_data():
    csv = open("cases.csv", mode="r")
    lines = csv.readlines()

    countries = []
    country_data = []
    for i in range(len(lines)):
        line = lines[i].split(",")
        if line[1] in countries:
            # this isn't really needed anymore, since this was used in the process of updating the dataset, but I'll keep it
            ind = countries.index(line[1])
            for j in range(data_start, len(country_data[ind])):
                country_data[ind][j] += float(line[j])
        else:
            countries.append(line[1])
            line[0] = float(line[0])
            for j in range(data_start, len(line)):
                line[j] = float(line[j])
            country_data.append(line)

    return country_data

def get_usable_data(line):
    pop = line[0]
    data = [] # in ppl per million, by date 1st date starts at index 0
    for i in range(data_start, len(line)):
        data.append(1000000*(line[i] / pop))

    return data

def get_name_cpm_data():
    data = get_data()
    name_data_arrays = []
    for i in range(len(data)):
        name = data[i][1]
        pop = data[i][0]
        if pop >= population_minimum:
            ppm = get_usable_data(data[i])
            name_data_arrays.append([name, ppm, random_color()])

    return name_data_arrays

def random_color():
    return color_rgb(random.randint(100,255),random.randint(100,255),random.randint(100,255))

################
### Graphics ###
################
def create_win():
    win = GraphWin("", w,h, autoflush=False)
    title = Text(Point(w/2, 25), "COVID Confirmed Cases Per 1M Population")
    title.setFace("arial")
    title.setSize(25)

    sub = Text(Point(w/2, h-25), "Minimum of " + str(population_minimum) + " people")

    sub.draw(win)
    title.draw(win)

    win.update()

    return win

plot_width = w-180
plot_height = h-100

def new_frame(index):

    bg = Rectangle(Point(130,50), Point(w-50, h-50))
    bg.setFill(color_rgb(230,230,230))
    bg.setOutline(color_rgb(230,230,230))
    la = Line(Point(130,50), Point(130, h-50))
    ws = Rectangle(Point(0,50),Point(129,h-50))
    ws.setFill("white")
    ws.setOutline("white")
    rws = Rectangle(Point(w-50,50),Point(w,h-50))
    rws.setOutline("white")
    rws.setFill("white")
    dl = Text(Point(w-200,h-100), dates[index])
    dl.setSize(15)

    rws.draw(window)
    ws.draw(window)
    bg.draw(window)
    la.draw(window)
    dl.draw(window)
    # window.update()

def draw_time(index):
    new_frame(index)
    date_text = dates[index]
    time_2d_list = []
    for i in range(len(name_cpm_data)):
        time_2d_list.append([name_cpm_data[i][0],name_cpm_data[i][1][index], name_cpm_data[i][2]])

    time_2d_list = sorted(time_2d_list, key=lambda x: x[1], reverse=True)

    selected_time_2d_list = time_2d_list[:num_countries_in_graph]
    space_per_bar = plot_height / num_countries_in_graph
    multiplier = plot_width / selected_time_2d_list[0][1]


    for i in range(len(selected_time_2d_list)):
        p1 = Point(130,50+i*space_per_bar)
        p2 = Point(130+multiplier * selected_time_2d_list[i][1], 50+(i+1)*space_per_bar)
        r = Rectangle(p1,p2)
        r.setFill(selected_time_2d_list[i][2])
        label = Text(Point(130/2, 0.5*(p1.y+p2.y)),selected_time_2d_list[i][0])
        label.setSize(9)
        val = Text(Point(p2.x - 20, 0.5*(p1.y+p2.y)), round(selected_time_2d_list[i][1], 2))
        r.draw(window)
        label.draw(window)
        val.draw(window)

    window.update()


window = create_win()

name_cpm_data = get_name_cpm_data() #each index looks like ['country name', [0,0.01,0.02,0.3,0.4 ...]]

window.getMouse()

for k in range(len(dates)):
    draw_time(k)
    time.sleep(0.5)

window.getMouse()
window.close()
