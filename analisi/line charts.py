# -*- coding: utf-8 -*-
"""
Created by Francesco Mattioli
Francesco@nientepanico.org
www.nientepanico.org
"""

import pandas as pd
import numpy as np
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats

def datiregioni_csv(mm,gg):
    grezzi = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-2020" + mm + gg + ".csv")
    return grezzi


def regioni_json():
    grezzi = pd.read_json("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json")
    return grezzi

raw = regioni_json()



fig = go.Figure()
fig.add_trace(go.Scatter(x=raw.data, y=raw['totale_casi'], name="totale_casi",
                         line_color='deepskyblue'))

fig.add_trace(go.Scatter(x=raw.data, y=raw['deceduti'], name="deceduti"))

fig.add_trace(go.Scatter(x=raw.data, y=raw['deceduti'], name="totale_casi"))


fig.update_layout(title_text='Time Series with Rangeslider',
                  xaxis_rangeslider_visible=True)



plot(fig)
 