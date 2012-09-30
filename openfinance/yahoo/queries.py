import requests
import copy


class Yahoo(object):
    """
    Base class for querying the Yahoo! finance API.

    The Yahoo! finance api is driven by their propietary query
    language, YQL, and is callable via URL referrers

    The data available is based on the open source community tables

    All of the queries here are derived from
    https://github.com/yql/yql-tables/tree/master/yahoo/finance
    """
    base_url = 'http://query.yahooapis.com/v1/public/yql'

    queries = {
        'quotes': {
            'table': 'yahoo.finance.quotes',
            'statement': 'select * from {} where symbol in ({})',
            'params': [(list, 'symbols')]
        },
        'options': {
            'table': 'yahoo.finance.options',
            'statement': 'select * from {} where symbol = "{}" and expiration = "{}"',
            'params': [(str, 'symbol'), (str, 'expiration')]
        },
        'sectors': {
            'table': 'yahoo.finance.sectors',
            'statement': 'select * from {}',
            'params': []
        },
        'industry': {
            'table': 'yahoo.finance.industry',
            'statement': 'select * from {} where id = "{}"',
            'params': [(str, 'industry_id')]
        }
    }

    default_params = {
         'format': 'json',
         'env': 'store://datatables.org/alltableswithkeys',
    }

    def _query(self, query_type, *params):
        """
        Make a query against the YQL API.
        """

        table = self.queries[query_type]['table']
        statement = self.queries[query_type]['statement'].format(
            table,
            *params
        )
        url_params = copy.copy(self.default_params)
        url_params.update({'q': statement})
        response = requests.get(self.base_url, params=url_params)

        if response.status_code is not requests.codes.ok:
            raise Exception("Status code is %s.\n%s" % (response.status_code,
                response.text))

        return(response.json)

    def show_query(self, query_type):
        """
        Prints meta information about the query
        """
        print(self.queries[query_type]['statement'].format(
            self.queries[query_type]['table'],
            *self.queries[query_type]['params']
        ))

    def get_quotes(self, symbols):
        """
        Get stock quotes
        """
        # Retrieve a list of stock symbols from the kwargs

        quotes = ','.join(['"%s"' % value for value in symbols])

        return(self._query('quotes', quotes))

    def get_options(self, symbol, expiration):
        """
        Get options for a quote based on expiration date
        """
        return(self._query('options', symbol, expiration))

    def get_sectors(self):
        """
        Get a list of all available sectors (industries)

        Does not accept any parameters
        """
        return(self._query('sectors'))

    def get_industry(self, industry_id):
        """
        Get a list of ticker symbols from an industry.
        """
        return(self._query('industry', industry_id))
