from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects = True)
    assert_equal(rv.status_code, 200)
    # assert_in(b"Fill Out This Form", rv.data)

    data = {'name': 'ASIF HOSSAIN', 'email': 'hossainasif502@gmail.com', 'massage': 'This is a teasting massage'}
    rv = web.post('/', follow_redirects = True, data = data)
    assert_in(b"ASIF HOSSAIN", rv.data)
    assert_in(b"hossainasif502@gmail.com", rv.data)
    assert_in(b"This is a teasting massage", rv.data)