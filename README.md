# covid-chart-race
I've seen many chart races about the number of people infected in a country, but I think this statistic doesn't fully tell the story.

Instead, the per capita statistic, in my opinion, is a lot better. Thus, I created this chart race through May 15, 2020 with the main statistic being the number of infections per million population.

## Usage
The uploaded ```cases.csv```, ```script.py``` and ```graphics.py``` are enough to run the graphical program. Run ```script.py```

However, this will only run the data through May 15. In order to ease the whole process, the original Johns Hopkins dataset was edited a little bit (to include the country's population, for example). To edit and intialize the sheet, use ```getting_country_populations.py```.

Population data was gathered from [worlddatasoft](https://data.opendatasoft.com/explore/dataset/world-population@kapsarc/api/)
Infected data was gathered from Johns Hopkins University

## Variables
**Population Minimum:** the ```population_minimum``` variable is the minimum population for a country to be included.

**Number of Countries:** the ```num_countres_in_graph``` variable dictates the number of countries that make the charts, and are included in the graphical interface.
