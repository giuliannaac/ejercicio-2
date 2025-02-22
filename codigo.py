import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
!pip install gapminder
from gapminder import gapminder
penguins = sns.load_dataset('penguins')
penguins
px.box(penguins,x="species",y="flipper_length_mm",color="species")
px.box(penguins,x="sex",y="flipper_length_mm",color="sex")
