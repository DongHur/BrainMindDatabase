import numpy as np
import matplotlib
'exec(%matplotlib inline)'
from collections import Counter
from itertools import groupby
from itertools import chain
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import chart_studio.plotly as py
from plotly.subplots import make_subplots

class MaturityLevel():
    def __init__(self):
        self.test='test'
    def maturity_vs_category(self, mat_cat_list, plot_type='plotly'):
        # group by category
        data = {}
        labels = []
        sizes = []
        subplot_titles = []
        sorted_list = sorted(mat_cat_list, key=lambda row: (row[1]) if len(row)>1 else ' ')
        for category, cat_rows in groupby(sorted_list, lambda x: x[1] if len(x)>1 else ' '):
            if category != '' and category != ' ':
                for maturity, mat_rows in groupby(list(cat_rows), lambda x: x[0] if len(x)>0 else ' '):
                    if maturity != ' ' and maturity != '' and maturity != 'N/A':
                        sizes.append(len(list(mat_rows)))
                        labels.append(maturity)
                data[category] = [sizes[:], labels[:]]
                subplot_titles.append(category)
        # plot data
        if plot_type == 'plotly':
            domain = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}], 
                    [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]
            fig = make_subplots(rows=2, cols=3, specs=domain, subplot_titles=subplot_titles[:7])
            for idx, (key, value) in enumerate(data.items()):
                # print(key)
                if idx+1<4:
                    print(idx+1)
                    print(value)
                    fig.add_trace(go.Pie(labels=value[1], values=value[0], name=key, text=value[1]),
                    1,idx+1)
                elif idx+1<7:
                    fig.add_trace(go.Pie(labels=value[1], values=value[0], name=key, text=value[1]),
                    2,idx-2)
            fig.update_layout(title_text="Maturity vs Category")
            py.plot(fig, filename = 'Maturity vs Category', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('Maturity vs Category.png')
        pass

    def maturity_vs_tag(self, mat_tag_list, plot_type='plotly'):
        # group by tag
        data = {}
        labels = []
        sizes = []
        subplot_titles = []

        sorted_list = sorted(mat_tag_list, key=lambda row: (row[4]) if len(row)>4 else (' '))
        for tag1, tag1_rows in groupby(sorted_list, lambda x: x[4] if len(x)>4 else ' '):
            if tag1 != '' and tag1 != ' ':
                for maturity, mat_rows in groupby(list(tag1_rows), lambda x: x[0] if len(x)>0 else ' '):
                    if maturity != ' ' and maturity != '':
                        sizes.append(len(list(mat_rows)))
                        labels.append(maturity)
                print(":: ", tag1)
                data[tag1] = [sizes[:], labels[:]]
                subplot_titles.append(tag1)

        sorted_list = sorted(mat_tag_list, key=lambda row: (row[5]) if len(row)>5 else (' '))
        for tag2, tag2_rows in groupby(sorted_list, lambda x: x[5] if len(x)>5 else ' '):
            if tag2 != ' ' and tag2 != '':
                for maturity, mat_rows in groupby(list(tag2_rows), lambda x: x[0] if len(x)>0 else ' '):
                    if maturity != ' ' and maturity != '':
                        sizes.append(len(list(mat_rows)))
                        labels.append(maturity)
                if tag2 in list(data.keys()):
                    for new_idx, label in enumerate(labels):
                        if label in data[tag2][1]:
                            old_idx = data[tag2][1].index(label)
                            data[tag2][0][old_idx] += sizes[new_idx]
                        else:
                            data[tag2].append([sizes[new_idx], label])
                else:
                    print("&& ", tag2)
                    data[tag2] = [sizes[:], labels[:]]
                    subplot_titles.append(tag2)

        # plot data
        if plot_type == 'plotly':
            domain = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}], 
                    [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]
            fig = make_subplots(rows=2, cols=3, specs=domain, subplot_titles=subplot_titles[:7])
            print("Subplot Title: ", subplot_titles)
            for idx, (key, value) in enumerate(data.items()):
                if idx+1<4:
                    fig.add_trace(go.Pie(labels=value[1], values=value[0], name=key, text=value[1]),
                    1,idx+1)
                elif idx+1<7:
                    fig.add_trace(go.Pie(labels=value[1], values=value[0], name=key, text=value[1]),
                    2,idx-2)
            fig.update_layout(title_text="Maturity vs Tag")
            py.plot(fig, filename = 'Maturity vs Tag', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('Maturity vs Tag.png')
        pass

    def maturity_vs_subtag(self, mat_subtag_list, plot_type='plotly'):
        # group by tag
        data = {}
        labels = []
        sizes = []
        subplot_titles = []
        first_subtag = 6
        second_subtag = 7
        last_subtag = 12
        # first subtag
        sorted_list = sorted(mat_subtag_list, key=lambda row: (row[first_subtag]) if len(row)>first_subtag else (' '))
        for subtag1, subtag1_rows in groupby(sorted_list, lambda x: x[first_subtag] if len(x)>first_subtag else ' '):
            if subtag1 != ' ' and subtag1 != '':
                for maturity, mat_rows in groupby(list(subtag1_rows), lambda x: x[0] if len(x)>0 else ' '):
                    if maturity != ' ' and maturity != '':
                        sizes.append(len(list(mat_rows)))
                        labels.append(maturity)
                print(":: ", subtag1)
                data[subtag1] = [sizes[:], labels[:]]
                subplot_titles.append(subtag1)
        # following subtag
        for sub_idx in range(second_subtag, last_subtag):
            sorted_list = sorted(mat_subtag_list, key=lambda row: (row[sub_idx]) if len(row)>sub_idx else (' '))
            for subtag2, subtag2_rows in groupby(sorted_list, lambda x: x[sub_idx] if len(x)>sub_idx else ' '):
                if subtag2 != ' ' and subtag2 != '':
                    for maturity, mat_rows in groupby(list(subtag2_rows), lambda x: x[0] if len(x)>0 else ' '):
                        if maturity != ' ' and maturity != '':
                            sizes.append(len(list(mat_rows)))
                            labels.append(maturity)
                    if subtag2 in list(data.keys()):
                        for new_idx, label in enumerate(labels):
                            if label in data[subtag2][1]:
                                old_idx = data[subtag2][1].index(label)
                                data[subtag2][0][old_idx] += sizes[new_idx]
                            else:
                                data[subtag2].append([sizes[new_idx], label])
                    else:
                        print("&& ", subtag2)
                        data[subtag2] = [sizes[:], labels[:]]
                        subplot_titles.append(subtag2)

        # plot data
        if plot_type == 'plotly':
            domain = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}], 
                    [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]
            fig = make_subplots(rows=2, cols=3, specs=domain, subplot_titles=subplot_titles[:7])
            print("Subplot Title: ", subplot_titles)
            for idx, (key, value) in enumerate(data.items()):
                if idx+1<4:
                    fig.add_trace(go.Pie(labels=value[1], values=value[0], name=key, text=value[1]),
                    1,idx+1)
                elif idx+1<7:
                    fig.add_trace(go.Pie(labels=value[1], values=value[0], name=key, text=value[1]),
                    2,idx-2)
            fig.update_layout(title_text="Maturity vs Subtag")
            py.plot(fig, filename = 'Maturity vs Subtag', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('Maturity vs Subtag.png')
        pass
