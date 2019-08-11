import numpy as np
import matplotlib
'exec(%matplotlib inline)'
from collections import Counter
from itertools import groupby
from itertools import chain
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objects as go

class Funding():
    def __init__(self):
        self.test='test'
    def funding_pie(self, funding_list, plot_type='plotly'):
        funding_list = funding_list[0]+funding_list[1]
        funding_list = [[fund.strip() for fund in funding_string.split(',')] for funding_string in funding_list]
        funding_count = Counter(list(chain.from_iterable(funding_list))) # {'blue': 3, 'red': 2, 'yellow': 1}
        print(funding_count)
        print()
        labels = []
        sizes = []
        texts = []
        for idx, (funding, count) in enumerate(funding_count.items()):
            if funding != 'n/a' and funding != '' and funding != '--':
                # if len(funding) > 12:
                #     # print([fund.strip() for fund in funding.split(',')])
                #     labels.append([fund.strip() for fund in funding.split(',')])
                # else:
                labels.append(idx)
                texts.append(funding)
                sizes.append(count)
        if plot_type == 'plotly':
            fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, 
                name='Volume of Each Investor', text=texts)])
            fig.update_layout(title=go.layout.Title(text="Volume of Each Investor"))
            py.plot(fig, filename = 'Volume of Each Investor', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('Volume of Each Investor.png')
        pass
    def investor_vs_category(self, cat_inv_list, plot_type='plotly'):
        # group by category
        labels = []
        sizes = []
        texts = []
        sorted_list = sorted(cat_inv_list, key=lambda row: (row[0]) if len(row)>0 else (' '))
        cat_idx = 0
        for category, rows in groupby(sorted_list, lambda x: x[0] if len(x)>0 else (' ')):
            count = 0
            for row in rows:
                for idx in range(1, len(row)):
                    count += len(row[idx].split(','))
            labels.append(cat_idx)
            sizes.append(count)
            texts.append(category)
            print(cat_idx, ":: ", category)
            cat_idx += 1
        # plot data
        if plot_type == 'plotly':
            fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, 
                name='Category vs Investor', text=texts)])
            fig.update_layout(title=go.layout.Title(text="Category vs Investor"))
            py.plot(fig, filename = 'Category vs Investor', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('Category vs Investor.png')
        pass
    def investor_vs_tag(self, tag_inv_list, plot_type='plotly'):
        # group by tags
        labels = []
        sizes = []
        texts = []

        sorted_list = sorted(tag_inv_list, key=lambda row: (row[2]) if len(row)>2 else (' '))
        tag_idx = 0
        for tag1, rows in groupby(sorted_list, lambda x: x[2] if len(x)>2 else ' '):
            count = 0
            for row in rows:
                for idx in range(1, len(row)):
                    count += len(row[idx].split(','))
            if tag1 != ' ' and tag1 != '' and tag1 != 'n/a':
                labels.append(tag_idx)
                texts.append(tag1)
                sizes.append(count)
                tag_idx += 1
            print(":: ", tag1)

        sorted_list = sorted(tag_inv_list, key=lambda row: (row[3]) if len(row)>3 else (' '))
        for tag2, rows in groupby(sorted_list, lambda x: x[3] if len(x)>3 else ' '):
            count = 0
            for row in rows:
                for idx in range(1, len(row)):
                    count += len(row[idx].split(','))
            if tag2 != ' ' and tag1 != '' and tag1 != 'n/a':
                if tag2 in labels:
                    idx = labels.index(tag2)
                    sizes[idx] += count
                else:
                    print("&& ", tag2)
                    labels.append(tag_idx)
                    texts.append(tag2)
                    sizes.append(count)
                    tag_idx += 1
        # plot data
        if plot_type == 'plotly':
            fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, 
                name='Tag vs Investor', text=texts)])
            fig.update_layout(title=go.layout.Title(text="Tag vs Investor"))
            py.plot(fig, filename = 'Tag vs Investor', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('Tag vs Investor.png')
        pass

    def investor_type_vs_each_category(self, cat_inv_list, inv_type_list, plot_type='plotly'):
        category_list = cat_inv_list[0]
        investor1_list = [x.lower() for x in cat_inv_list[1]]
        coinvestor1_list = [x.lower() for x in cat_inv_list[2]]
        investor2_list = [x.lower() for x in inv_type_list[0]]
        type_list = inv_type_list[1]

        print("len(category_list): ", len(category_list))
        print("len(investor1_list): ", len(investor1_list))
        print("len(coinvestor1_list): ", len(coinvestor1_list))
        print("len(investor2_list): ", len(investor2_list))
        print("len(type_list): ", len(type_list))
        data = {}
        count = 0
        for idx, category in enumerate(category_list):
            if category == "" or category == " " or category == "n/a":
                continue
            if category not in data.keys():
                data[category] = {}

            # parse through investor column in Neuro Companies
            if idx<len(investor1_list) and investor1_list[idx] != "" and investor1_list[idx] != "n/a":
                for investor in investor1_list[idx].split(","):
                    investor = investor.strip().lower()
                    if investor == "" or investor == "--" or investor == "n/a":
                        continue
                    if investor in investor2_list:
                        count += 1
                        inv2_idx = investor2_list.index(investor)
                        inv_type = type_list[inv2_idx]
                        if inv_type not in data[category].keys():
                            data[category][inv_type] = 1
                        else:
                            data[category][inv_type] += 1
                    else:
                        print(":: not in investor list: ", investor)
            
            # parse through coinvestor column in Neuro Companies
            if idx<len(coinvestor1_list) and coinvestor1_list[idx] != "" and coinvestor1_list[idx] != "n/a":
                for investor in coinvestor1_list[idx].split(","):
                    investor = investor.strip().lower()
                    if investor == "" or investor == "--" or investor == "n/a":
                        continue
                    if investor in investor2_list:
                        count += 1
                        inv2_idx = investor2_list.index(investor)
                        inv_type = type_list[inv2_idx]
                        if inv_type not in data[category].keys():
                            data[category][inv_type] = 1
                        else:
                            data[category][inv_type] += 1
                    else:
                        print(":: not in investor list: ", investor)
        print("TOTAL Investors: ", count)

        categories = list(data.keys())
        # get all funding type into a list
        funding_type_list = []
        for key, values in data.items():
            funding_type_list = list(set(funding_type_list)|set(values.keys()))
        print(funding_type_list)   
        
        # get all y value for each funding type into a list
        fund_type_quantity = np.zeros((len(categories), len(funding_type_list)))
        for cat_idx, values in enumerate(data.values()):
            for ft_idx, funding_type in enumerate(funding_type_list):
                if funding_type in values.keys():
                    fund_type_quantity[cat_idx, ft_idx] = values[funding_type]
        # print(list(data.keys()))
        # print()
        # print(fund_type_quantity)
        # print()
        # print(data)

        # plot data
        if plot_type == 'plotly':
            go_data = []
            for i in range(len(funding_type_list)):
                go_data.append(go.Bar(name=funding_type_list[i], x=categories, y=fund_type_quantity[:,i]))
            fig = go.Figure(data=go_data)

            fig.update_layout(title_text="Investor Type for Each Category", barmode='stack')
            py.plot(fig, filename = 'Investor Type for Each Category', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('Investor Type for Each Category.png')
        pass

    def investor_type_vs_each_tag(self, tag_inv_list, inv_type_list, plot_type='plotly'):
        tag1_list = tag_inv_list[2]
        tag2_list = tag_inv_list[3]
        investor1_list = [x.lower() for x in tag_inv_list[0]]
        coinvestor1_list = [x.lower() for x in tag_inv_list[1]]
        investor2_list = [x.lower() for x in inv_type_list[0]]
        type_list = inv_type_list[1]

        print("len(tag1_list): ", len(tag1_list))
        print("len(tag2_list): ", len(tag2_list))
        print("len(investor1_list): ", len(investor1_list))
        print("len(coinvestor1_list): ", len(coinvestor1_list))
        print("len(investor2_list): ", len(investor2_list))
        print("len(type_list): ", len(type_list))
        data = {}
        count = 0
        # parse tag1
        for idx, tag in enumerate(tag1_list):
            if tag == "" or tag == " " or tag == "n/a":
                continue
            if tag not in data.keys():
                data[tag] = {}

            # parse through investor column in Neuro Companies
            if idx<len(investor1_list) and investor1_list[idx] != "" and investor1_list[idx] != "n/a":
                for investor in investor1_list[idx].split(","):
                    investor = investor.strip().lower()
                    if investor == "" or investor == "--" or investor == "n/a":
                        continue
                    if investor in investor2_list:
                        count += 1
                        inv2_idx = investor2_list.index(investor)
                        inv_type = type_list[inv2_idx]
                        if inv_type not in data[tag].keys():
                            data[tag][inv_type] = 1
                        else:
                            data[tag][inv_type] += 1
                    else:
                        print(":: not in investor list: ", investor)
            
            # parse through coinvestor column in Neuro Companies
            if idx<len(coinvestor1_list) and coinvestor1_list[idx] != "" and coinvestor1_list[idx] != "n/a":
                for investor in coinvestor1_list[idx].split(","):
                    investor = investor.strip().lower()
                    if investor == "" or investor == "--" or investor == "n/a":
                        continue
                    if investor in investor2_list:
                        count += 1
                        inv2_idx = investor2_list.index(investor)
                        inv_type = type_list[inv2_idx]
                        if inv_type not in data[tag].keys():
                            data[tag][inv_type] = 1
                        else:
                            data[tag][inv_type] += 1
                    else:
                        print(":: not in investor list: ", investor)
        
        # parse tag2
        for idx, tag in enumerate(tag2_list):
            if tag == "" or tag == " " or tag == "n/a":
                continue
            if tag not in data.keys():
                data[tag] = {}

            # parse through investor column in Neuro Companies
            if idx<len(investor1_list) and investor1_list[idx] != "" and investor1_list[idx] != "n/a":
                for investor in investor1_list[idx].split(","):
                    investor = investor.strip().lower()
                    if investor == "" or investor == "--" or investor == "n/a":
                        continue
                    if investor in investor2_list:
                        count += 1
                        inv2_idx = investor2_list.index(investor)
                        inv_type = type_list[inv2_idx]
                        if inv_type not in data[tag].keys():
                            data[tag][inv_type] = 1
                        else:
                            data[tag][inv_type] += 1
                    else:
                        print(":: not in investor list: ", investor)
            
            # parse through coinvestor column in Neuro Companies
            if idx<len(coinvestor1_list) and coinvestor1_list[idx] != "" and coinvestor1_list[idx] != "n/a":
                for investor in coinvestor1_list[idx].split(","):
                    investor = investor.strip().lower()
                    if investor == "" or investor == "--" or investor == "n/a":
                        continue
                    if investor in investor2_list:
                        count += 1
                        inv2_idx = investor2_list.index(investor)
                        inv_type = type_list[inv2_idx]
                        if inv_type not in data[tag].keys():
                            data[tag][inv_type] = 1
                        else:
                            data[tag][inv_type] += 1
                    else:
                        print(":: not in investor list: ", investor)
        print("TOTAL Investors: ", count)

        tags = list(data.keys())
        # get all funding type into a list
        funding_type_list = []
        for key, values in data.items():
            funding_type_list = list(set(funding_type_list)|set(values.keys()))
        print(funding_type_list)   
        
        # get all y value for each funding type into a list
        fund_type_quantity = np.zeros((len(tags), len(funding_type_list)))
        for cat_idx, values in enumerate(data.values()):
            for ft_idx, funding_type in enumerate(funding_type_list):
                if funding_type in values.keys():
                    fund_type_quantity[cat_idx, ft_idx] = values[funding_type]
        print("************")
        print(tags)
        print()
        print(fund_type_quantity)
        print()
        print(data)

        # plot data
        if plot_type == 'plotly':
            go_data = []
            for i in range(len(funding_type_list)):
                go_data.append(go.Bar(name=funding_type_list[i], x=tags, y=fund_type_quantity[:,i]))
            fig = go.Figure(data=go_data)

            fig.update_layout(title_text="Investor Type for Each Tags", barmode='stack')
            py.plot(fig, filename = 'Investor Type for Each Tags', auto_open=True)
            # fig.show()
        elif plot_type == 'matplotlib':
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels)
            ax1.axis('equal')
            fig1.savefig('Investor Type for Each Tags.png')
        pass
    def company_per_investor(self, tag_inv_list):
        tag_inv_list = np.array(tag_inv_list)
        # parameter
        cutoff = 20
        # parse top few companies
        num_company_invested = np.array([len(row)-2 for row in tag_inv_list if row[0]])
        # print(num_company_invested)
        idx_sorted = sorted(range(len(num_company_invested)), 
            key=lambda k: num_company_invested[k], reverse=True)
        # print()
        # print(idx_sorted)
        idx_top_sorted = idx_sorted[:cutoff]

        investor = [row[0] for row in tag_inv_list[idx_top_sorted]]
        num_comp = num_company_invested[idx_top_sorted]
        print(investor)
        print(num_comp)
        fig = go.Figure([go.Bar(x=investor, y=num_comp)])
        fig.update_layout(title_text="Number of Companies Invested in For Top 20 Companies")
        py.plot(fig, filename = 'Number of Companies Invested in For Top 20 Companies', auto_open=True)
        # fig.show()
        pass











