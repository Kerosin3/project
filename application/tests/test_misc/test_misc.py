# from application import a
# from application import app
from application.misc import get_data_historical,get_lastday_data,get_today_price
import pytest
from pandas._libs.tslibs.timestamps import Timestamp
from iexfinance.utils.exceptions import  IEXQueryError
from application.misc import ServerExeption,SomethingBadHappened,NoSuchStock
from app import app
# @pytest.fixture
# def client():
#     with app.test_client() as test_client:
#         with app.app_context():
#             yield test_client

def test_stock_getter_lastday():
    ticker = 'TSLA'
    price,volume = get_lastday_data(ticker)
    assert price is not None
    assert type(price) == float
    assert type(volume) == int

def test_stock_getter_historical_data():
    ticker = 'TSLA'
    prices,volume = get_data_historical(ticker)
    for date,price in prices.items():
        print(f'price at date {date} was {price}')
        assert type(date) == Timestamp
        assert type(price) == float or type(price) == int

def test_today_price():
    ticker = 'TSLA'
    price = get_today_price(ticker)
    # print('current price is', price)
    assert type(price) == float or type(price) == int

def test_today_price_not_existsable_stock():
    '''IEXQueryError error'''
    ticker = 'xxxx'
    price = get_today_price(ticker)
    assert price == None

def test_today_price_not_existsable_stock_failure():
    """
    i.e stock exists
    :return:
    """
    ticker = 'TSLA'
    price = get_today_price(ticker)
    assert price is not None

def test_today_price_not_existsable_stock_failure_unknown():
    ticker = ''
    with pytest.raises(NoSuchStock):
        price = get_today_price(ticker)