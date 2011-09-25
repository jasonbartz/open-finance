# Libraries
import urllib
# OpenFinance
from openfinance import openFinance

# set initial query_params_dict values
QUERY_PARAMS_DICT = {
     'format': 'json',
     'env':'store://datatables.org/alltableswithkeys',
     'callback':'finance_query',
}

class openFinanceYahoo(openFinance):
    '''
    Base class for querying the Yahoo! finance API.
    
    The Yahoo! finance api is driven by their propietary query language, YQL, and is callable via URL referrers
    
    The data available is based on the open source community tables
    
    All of the queries here are derived from https://github.com/yql/yql-tables/tree/master/yahoo/finance
    '''

    
    def get_quotes(self):
        # Retrieve a list of stock symbols from the kwargs
        try:
            quote_list = self.kwargs['quote_list'] 
        except KeyError:
            print "You did not pass a quote list kwarg. You should literally pass\
                    a python list into the kwarg quote_list.\n  You passed: %s" % self.kwargs
        
        quotes = ','.join(['"%s"' % value for value in quote_list])
        
        # Set the query table and statement
        query_table = 'yahoo.finance.quotes'
        
        query_statement = 'select * from %s where symbol in (%s)' % (query_table, quotes)
       
        
        query_url = 'http://query.yahooapis.com/v1/public/yql'
        QUERY_PARAMS_DICT['q'] = query_statement
        query_params = urllib.urlencode(QUERY_PARAMS_DICT)
        
        query_url = '%s?%s' % (query_url,query_params)
        
        self.kwargs['query_url'] = query_url
    
        query = self._query(**self.kwargs)
    
        return query
    def get_options(self):
        pass
    def get_sectors_list(self):
        pass
    def get_industry_list(self):
        pass