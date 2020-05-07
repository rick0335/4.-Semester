import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://thejokerd3:sxp78gaf@breaktimeawarenesscluster-rwpry.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["BreakTimeDB"]
collection = db["BreakTimeCollection"]

df = pd.DataFrame(list(collection.find()))

plt.style.use('ggplot')

#Vi vil gerne finde ude af typen af vores datasæt
print("Dette er typen af vores datasæt")
print(type(df))

#Vi printer ud vores shape på vores datasæt for at se hvor mange datapunkter vi har og hvor mange features vi har.
print("Antallet af datapunkter og features i vores datasæt")
print(df.shape)

del df['_id']

fig = plt.scatter(df,
    dimensions=["hours_slept", "light_level", "temperature_level", "noise_level"],
    color="needs_pause")
fig.show()

