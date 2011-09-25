#Libraries
import scrapelib


__version__ = 'version 0.0.1 *alpha'
_user_agent = 'openfinance %s' % __version__

class openFinance(object):
    '''
    This is the base class from which all query classes inherit.  
    
    It is designed to abstract out the basest of needs for any queryset
    
    As a template, it lists out the needs of the types of methods that can be overwritten in inherited classes
    '''
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        
    def _query(self):
        '''
        Can accept a number of parameters that define a query, including the desired URL or URL parameters
        '''
        try:
            query_url = self.kwargs['query_url']
        except:
            print 'No query URL passed, please assign one via the query_url keyword argument'
        
        # rewrite to follow proper directory rules
        cache_root = '/Users/bartzj/Code/jason/open-finance/cache'
        
        # instantiate the scrapelib scraper
        # enabling cache, but allowing scrapelib to evaluate headers and fetch new data if it exists
        # currently set to 60 requests per minute max
        self.scraper = scrapelib.Scraper(follow_robots=False,
                                        cache_dir=cache_root,
                                        requests_per_minute=60)

        # Run the scraper against the passed URL
        query = self.scraper.urlopen(query_url, method='GET')
        
        # Return the raw html to the buffer
        return query
        
    def _parse(self):
        '''
        Will parse a returned query object into a python dictionary.
        
        Most dictionaries will follow the same format
        '''
        query_object = self._query()
        return query_object
        
    def return_data(self):
        '''
        Returns data to the buffer
        '''
        queried_data = self._parse()
        return queried_data
        