from unittest import TestCase
from openfinance.yahoo import api
import datetime


class TestYahoo(TestCase):

    def run_query_tests(self):
        """
        Run the tests associated with this api suite.
        """
        # Test ``<meth: get_quotes>get_quotes``
        quotes = api.get_quotes(["yhoo", "msft"])

        self.assertEquals(type(quotes), dict)
        self.assertEquals(len(quotes['query'].keys()), 4)
        self.assertEquals(len(quotes['query']['results']['quote']), 2)
        self.assertEquals(quotes['query']['results']['quote'][0]['symbol'],
            u'YHOO')
        self.assertEquals(quotes['query']['results']['quote'][1]['symbol'],
            u'MSFT')

        # Test ``<meth: get_options>get_options``
        expiration = datetime.datetime.strftime(datetime.datetime.now(),
            '%Y-%m')
        options = api.get_options('yhoo', expiration)
        self.assertEquals(type(options), dict)
        self.assertEquals(len(options['query'].keys()), 4)
        self.assertEquals(options['query']['results']['optionsChain']['expiration'],
            expiration)

        # Test ``<meth: get_sectors>get_sectors``
        sectors = api.get_sectors()
        self.assertEquals(type(sectors), dict)
        self.assertEquals(len(sectors['query'].keys()), 4)
        # Assumes that there are nine or more industries, this test may
        # need to be more robust.
        self.assertGreaterEqual(len(sectors['query']['results']['sector']), 9)

        # Test ``<meth: get_industry>get_industry``
        industry = api.get_industry("112")
        self.assertEquals(type(industry), dict)
        self.assertEquals(len(industry['query'].keys()), 4)
        # Assumes that there are more than two companies in this industry
        # This test may need to be more robust.
        self.assertGreaterEqual(industry['query']['results']['industry']['company'],
            2)
