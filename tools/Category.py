import numpy as np
import matplotlib
'exec(%matplotlib inline)'
from collections import Counter
from itertools import groupby, combinations, chain
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import chart_studio.plotly as py
from plotly.subplots import make_subplots
import csv

class Category():
    def __init__(self):
        self.test='test'
    def category_pie(self, category_list, plot_type='plotly'):
        category_count = Counter(list(chain.from_iterable(category_list))) # {'blue': 3, 'red': 2, 'yellow': 1}
        labels = []
        texts = []
        sizes = []
        for idx, (category, count) in enumerate(category_count.items()):
            labels.append(idx)
            texts.append(category)
            sizes.append(count)
            print(category, ": ", idx)
        if plot_type == 'plotly':
            fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, text=texts)])
            fig.update_layout(title=go.layout.Title(text="Companies Per Category"))
            py.plot(fig, filename = 'Companies Per Category', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('companies_per_category.png')
        pass
    def tag_pie(self, tag_list, plot_type='plotly'):
        tag_list = np.array(tag_list[0]+tag_list[1])
        
        tag_count = Counter(tag_list) # {'blue': 3, 'red': 2, 'yellow': 1}
        print()
        labels = []
        texts = []
        sizes = []
        for idx, (tag, count) in enumerate(tag_count.items()):
            if tag:
                labels.append(idx)
                texts.append(tag)
                sizes.append(count)
                print(tag, ": ", idx)
        if plot_type == 'plotly':
            fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, text=texts)])
            fig.update_layout(title=go.layout.Title(text="Tag Prevalence"))
            py.plot(fig, filename = 'Tag Prevalence', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('tag_prevalence.png')
        pass
    def subtag_pie(self, subtag_list, plot_type='plotly'):
        data = []
        for subtag_col in subtag_list:
            data = data + subtag_col
        subtag_list = np.array(data)
        subtag_count = Counter(subtag_list) # {'blue': 3, 'red': 2, 'yellow': 1}
        print(subtag_count)
        print()
        labels = []
        sizes = []
        texts = []
        for idx, (subtag, count) in enumerate(subtag_count.items()):
            if subtag:
                labels.append(idx)
                texts.append(subtag)
                sizes.append(count)
                print(subtag, ": ", idx)
        if plot_type == 'plotly':
            fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, text=texts)])
            fig.update_layout(title=go.layout.Title(text="Subtag Prevalence"))
            py.plot(fig, filename = 'Subtag Prevalence', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('subtag_prevalence.png')
        pass
    def funding_per_category(self, fund_category_list, plot_type='plotly'):
        # group by category
        fundings = []
        labels = []
        sizes = []
        totRaised = 15

        sorted_list = sorted(fund_category_list, key=lambda row: (row[0]) if len(row)>0 else (' '))
        for category, rows in groupby(sorted_list, lambda x: x[0] if len(x)>0 else ' '):
            if category != ' ' and category != '' and category != 'n/a':
                fund = 0
                for row in rows:
                    print(row)
                    if (len(row)>totRaised and row[totRaised] != ' ' and row[totRaised] != '' and 
                    row[totRaised] != '—' and row[totRaised] != '--'):
                        print("TEST: ", row[totRaised])
                        fund += float(row[totRaised].split('$')[1])
                        print(fund)
                labels.append(category)
                fundings.append(fund)
                print(":: ", category)
        # plot data
        if plot_type == 'plotly':
            fig = go.Figure([go.Bar(x=labels, y=fundings)])
            fig.update_layout(title=go.layout.Title(text="Fuding Per Category"))
            py.plot(fig, filename = 'Fuding Per Category', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('Fuding Per Category.png')
        pass
    def network(self, company_list, category_list, tag_list, subtag_list, tot_raised_list):
        print("len(company_list): ", len(company_list))
        print("len(category_list): ", len(category_list))
        print("len(tag_list): ", len(tag_list))
        print("len(subtag_list): ", len(subtag_list))
        print()
        comp_len = len(company_list)
        # create node data
        node_list = [['Id', 'Label', 'Total Raised', 'Categories']]
        for idx in range(comp_len):
            company = company_list[idx][0]

            # total raised data
            if idx < len(tot_raised_list) and len(tot_raised_list[idx])!=0:
                total_raised = tot_raised_list[idx][0].replace('$','').replace(',','').strip()
                if total_raised=="—" or total_raised=="--"  or total_raised=="":
                    total_raised_text = "n/a"
                    total_raised_num = 0.0
                else:
                    total_raised_text = "$"+total_raised+"M"
                    total_raised_num = float(total_raised)
            else: 
                total_raised = "n/a"

            # category data
            if idx < len(category_list) and len(category_list[idx])!=0:
                category = category_list[idx][0]
            else: 
                category = "n/a"

            company = company + " ("+total_raised_text+")"
            node_list.append([idx+1, company, total_raised_num, category])

        # create edge data
        edge_weight_list = [['source','target','weight']]
        combination_list = list(combinations(range(comp_len), 2))
        for comb in combination_list:
            idx0 = comb[0]
            idx1 = comb[1]
            # distance parameter
            cat1 = category_list[idx0] if len(category_list)>idx0 else None
            cat2 = category_list[idx1] if len(category_list)>idx1 else None
            tag1 = tag_list[idx0] if len(tag_list)>idx0 else None
            tag2 = tag_list[idx1] if len(tag_list)>idx1 else None
            subtag1 = subtag_list[idx0] if len(subtag_list)>idx0 else None
            subtag2 = subtag_list[idx1] if len(subtag_list)>idx1 else None

            weight = self.similarity(company1=[cat1, tag1, subtag1],
                    company2=[cat2, tag2, subtag2])
            edge_weight_list.append([idx0+1, idx1+1, weight])
        # save data
        with open("data/node.csv",'w') as resultFile:
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerows(node_list)
        with open("data/edge.csv",'w') as resultFile:
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerows(edge_weight_list)
        pass

    def similarity(self, company1, company2):
        # Gower's General Similarity Measurement
        # company1 - [category, tag, subtag]
        cat_weight = 10.0
        tag_weight = 5.0
        subtag_weight = 2.0
        weight_thresh = 0.01

        sim = 0.0
        factors = 0.0
        # category similarity
        if company1[0]!=None and company2[0]!=None and company1[0]==company2[0]:
            sim += 1.0*cat_weight
        factors += cat_weight

        # tag similarity
        if company1[1]!=None and company2[1]!=None :
            sim_list = list(set(company1[1]) & set(company2[1]))
            tot_list = list(set(company1[1]) | set(company2[1]))
            sim += len(sim_list)*tag_weight
            factors += len(tot_list)*tag_weight
        else:
            factors += tag_weight
            # for tag in company1[1]:
            #     if tag not in company2[1]:
            #         sim += 1*tag_weight
            #     factors += tag_weight
        
        # subtag similarity
        if company1[2]!=None and company2[2]!=None:
            sim_list = list(set(company1[2]) & set(company2[2]))
            tot_list = list(set(company1[2]) | set(company2[2]))
            sim += len(sim_list)*subtag_weight
            factors += len(tot_list)*subtag_weight
            # for subtag in company1[2]: 
            #     if subtag not in company2[2]:
            #         sim += 1*subtag_weight
            #     factors += subtag_weight
        else:
            factors += subtag_weight
        # compute total weight
        weight = sim/factors
        if weight < weight_thresh:
            weight = 0
        # else:
        #     weight = np.exp(weight)
        return round(weight, 4)



















