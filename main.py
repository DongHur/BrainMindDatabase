from tools.Login import Login
from tools.CRUD import CRUD_obj

# tools for analyzing data
from tools.Category import Category
from tools.Funding import Funding
from tools.MaturityLevel import MaturityLevel
from tools.Miscellaneous import Miscellaneous

def main():
    # key parameters
    token_path = 'data/'
    SAMPLE_SPREADSHEET_ID = '17KGCDtprJp7WXUDBODk1uXRs3Po7XgZm8Mkm3ZAWrrI'
    # login to google spreadsheet
    creds = Login(token_path)

    # create datasheet object
    CRUD = CRUD_obj(creds=creds, sheet_id=SAMPLE_SPREADSHEET_ID)
    Cat = Category()
    Fund = Funding()
    Mat = MaturityLevel()
    Misc = Miscellaneous()
    
    # CATEGORY INFO
    if False:
        # read from data
        company_range, company_list = 'Neuro Companies!A2:A', None
        category_range, category_list = 'Neuro Companies!F2:F', None
        ranges = [company_range, category_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse data
        company_list = data_range[0]['values']
        category_list = data_range[1]['values']
        Cat.category_pie(category_list)
    if False:
        # read from data
        tag_range, tag_list = 'Neuro Companies!I2:J', None
        ranges = [tag_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='COLUMNS')
        # parse data
        tag_list = data_range[0]['values']
        Cat.tag_pie(tag_list)
    if False:
        # read from data
        subtag_range, subtag_list = 'Neuro Companies!K2:Q', None
        ranges = [subtag_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='COLUMNS')
        # parse data
        subtag_list = data_range[0]['values']
        Cat.subtag_pie(subtag_list)
    if False:
        # read from data
        fund_category_range, fund_category_list = 'Neuro Companies!G2:U', None
        ranges = [fund_category_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse data
        fund_category_list = data_range[0]['values']
        Cat.funding_per_category(fund_category_list)
    if False:
        # read from data
        company_range, company_list = 'Neuro Companies!A2:A', None
        category_range, category_list = 'Neuro Companies!F2:F', None
        tag_range, tag_list = 'Neuro Companies!I2:J', None
        subtag_range, subtag_list = 'Neuro Companies!K2:Q', None
        tot_raised_range, tot_raised_list = 'Neuro Companies!U2:U', None
        ranges = [company_range, category_range, tag_range, subtag_range, tot_raised_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse datas
        company_list, category_list = data_range[0]['values'], data_range[1]['values']
        tag_list, subtag_list = data_range[2]['values'], data_range[3]['values']
        tot_raised_list = data_range[4]['values']
        Cat.network(company_list, category_list, tag_list, subtag_list, tot_raised_list)

        
    
    # INVESTOR INFO
    if False:
        # read from data
        investor_range, investor_list = 'Neuro Companies!G2:H', None
        ranges = [investor_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='COLUMNS')
        # parse data
        investor_list = data_range[0]['values']
        Fund.funding_pie(investor_list)
    if False:
        # read from data
        cat_inv_range, cat_inv_list = 'Neuro Companies!F2:H', None
        ranges = [cat_inv_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse data
        cat_inv_list = data_range[0]['values']
        Fund.investor_vs_category(cat_inv_list)
    if False:
        # read from data
        tag_inv_range, tag_inv_list = 'Neuro Companies!G2:J', None
        ranges = [tag_inv_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse data
        tag_inv_list = data_range[0]['values']
        Fund.investor_vs_tag(tag_inv_list)
    if False:
        # read from data
        cat_inv_range, cat_inv_list = 'Neuro Companies!F2:H', None
        inv_type_range, inv_type_list = 'Investors!A2:B', None
        ranges = [cat_inv_range, inv_type_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='COLUMNS')
        # parse data
        cat_inv_list = data_range[0]['values']
        inv_type_list = data_range[1]['values']
        Fund.investor_type_vs_each_category(cat_inv_list, inv_type_list)
    if False:
        # read from data
        tag_inv_range, tag_inv_list = 'Neuro Companies!G2:J', None
        inv_type_range, inv_type_list = 'Investors!A2:B', None
        ranges = [tag_inv_range, inv_type_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='COLUMNS')
        # parse data
        tag_inv_list = data_range[0]['values']
        inv_type_list = data_range[1]['values']
        Fund.investor_type_vs_each_tag(tag_inv_list, inv_type_list)
    if False:
        inv_range, inv_list = 'Investors!A2:AT', None
        ranges = [inv_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse data
        tag_inv_list = data_range[0]['values']
        Fund.company_per_investor(tag_inv_list)

    # MATURITY INFO
    if False:
        # read from data
        mat_cat_range, mat_cat_list = 'Neuro Companies!E2:F', None
        ranges = [mat_cat_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse data
        mat_cat_list = data_range[0]['values']
        Mat.maturity_vs_category(mat_cat_list)
    if False:
        # read from data
        mat_tag_range, mat_tag_list = 'Neuro Companies!E2:J', None
        ranges = [mat_tag_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse data
        mat_tag_list = data_range[0]['values']
        Mat.maturity_vs_tag(mat_tag_list)
    if False:
        # read from data
        mat_subtag_range, mat_subtag_list = 'Neuro Companies!E2:Q', None
        ranges = [mat_subtag_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse data
        mat_subtag_list = data_range[0]['values']
        Mat.maturity_vs_subtag(mat_subtag_list)

    # MISC INFO
    if False:
        # read from data
        year_cat_range, year_cat_list = 'Neuro Companies!F2:V', None
        ranges = [year_cat_range]
        data_range = CRUD.read(ranges=ranges, majorDimension='ROWS')
        # parse data
        year_cat_list = data_range[0]['values']
        Misc.companies_per_year(year_cat_list)




if __name__ == '__main__':
    main()

















