import numpy as np
from collections import Counter
from itertools import groupby
from itertools import chain
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objects as go
import dateutil.parser

class Miscellaneous():
    def __init__(self):
        self.test='test'

    def companies_per_year(self, year_cat_list):
        # print(year_cat_list) 
        sorted_cat_list = sorted(year_cat_list, key=lambda row: row[0] if len(row)>0 else (' '))
        # print(sorted_cat_list)
        categories = []
        time_list = []
        num_comp_list = []
        for cat, cat_rows in groupby(sorted_cat_list, lambda row: row[0] if len(row)>0 else (' ')):
            if cat == '' or cat == ' ' or cat == 'n/a':
                continue
            categories.append(cat)
            sorted_list = sorted(cat_rows, 
                key=lambda x: dateutil.parser.parse(x[16]).year if len(x)>16 and x[16]!='' and x[16].lower()!='n/a' else 0)
            # print(sorted_list)
            # print("\n\n\n\n")
            time = []
            num_comp = []
            for year, year_rows in groupby(sorted_list, 
                lambda x: dateutil.parser.parse(x[16]).year if len(x)>16 and x[16]!='' and x[16].lower()!='n/a' else 0):
                if year != 0:
                    # print(year, ": ", len(list(year_rows)))
                    time.append(year)
                    num_comp.append(len(list(year_rows)))
            time_list.append(time)
            num_comp_list.append(num_comp)
        
        # create figure
        fig = go.Figure()
        for idx, cat in enumerate(categories):
            fig.add_trace(go.Scatter(x=time_list[idx], y=num_comp_list[idx], mode='lines+markers', name=cat))
        fig.update_layout(title=go.layout.Title(text="Number of Neuro Companies for Each Category"),
                   xaxis_title='Years',
                   yaxis_title='Number of Companies')
        py.plot(fig, filename = 'Number of Neuro Companies for Each Category', auto_open=True)
        # fig.show()
        pass






















