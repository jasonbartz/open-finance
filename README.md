# open-finance

A python library that queries a series of freely available finance APIs to track, store information, and run analytics against this data. Currently supports:

* finance.yahoo.com (yql)

## finance.yahoo.com

The yahoo finance API is based off the data available from Yahoo's datatables. It abstracts the YQL into an easy-to-use python interface

### Basic usage

```python
from openfinance.yahoo import api
api.get_quotes(['yhoo'])
```

### Show query

Show query is designed to help you understand the parameters required for a query

```python
api.show_query('quotes')
```

### Available methods

* get_quotes - pass in a list of ticker symbols and get quote information
* get_options - pass in a ticker symbol and expiration to see available options
* get_sectors - retrieve a list of available sectors (industries)
* get_industry - pass in an industry id and retrieve a list of symbols that belong in that industry


## Changelog

### 0.0.2 alpha

#### Features

* refactored api to use requests, be more efficient
* added get_sectors, get_industry, get_options

