# Libraries

# OpenFinance
from openfinance.openfinance import openFinance

class openFinanceYahoo(openFinance):
    '''
    Base class for querying the Yahoo! finance API.
    
    The Yahoo! finance api is driven by their propietary query language, YQL, and is callable via URL referrers
    
    The data available is based on the open source community tables
    
    All of the queries here are derived from https://github.com/yql/yql-tables/tree/master/yahoo/finance
    '''
    
    def single_quote(self):
        pass
    def multiple_quotes(self):
        pass
    def get_options(self):
        pass
    def get_sectors_list(self):
        pass
    def get_industry_list(self):
        pass