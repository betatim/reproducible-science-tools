import matplotlib.pyplot as plt
import pandas as pd


def get_velo_data(location):
    fname = "bikes.csv"

    data = pd.read_csv(fname, parse_dates=True, dayfirst=True, index_col='Datum')

    # filter by location
    data = data[data.Standort == location]

    # subselect only the Velo data
    data = data[["Velo_in", "Velo_out"]]

    data['Total'] = data.Velo_in + data.Velo_out

    return data


mythenquai = get_velo_data('ECO09113499')
# rename for easier plotting
mythenquai.columns = ["North", "South", "Total"]

# Compute weekly rides by summing over the 15m intervals
weekly = mythenquai.resample('W').sum()
weekly.plot()

plt.savefig("weekly-2015.png")
