import pytest
from assignment import concert_calculator, codename_gen

@pytest.mark.parametrize( "ticket_price, num_tickets, sale_tax, processing_fee, expected", [
    (100, 3, 0.1, 5.50, "The price for 3 tickets at $100 each with 10.0% sales tax and $5.5 processing fee is $335.5"),
    (500, 3, 0.1, 5.50, "The price for 3 tickets at $500 each with 10.0% sales tax and $5.5 processing fee is $1655.5"),
    (100, 3, 0.5, 5.50, "The price for 3 tickets at $100 each with 50.0% sales tax and $5.5 processing fee is $455.5"),
    (100, 10, 0.1, 5.50, "The price for 10 tickets at $100 each with 10.0% sales tax and $5.5 processing fee is $1105.5"),
    (100, 3, 0.1, 10, "The price for 3 tickets at $100 each with 10.0% sales tax and $10 processing fee is $340.0"), 
    (1, 2, 0.15, 0.50, "The price for 2 tickets at $1 each with 15.0% sales tax and $0.5 processing fee is $2.8"), 
    (0, 3, 0.1, 5.50, "The price for 3 tickets at $0 each with 10.0% sales tax and $5.5 processing fee is $5.5"), 
    (100, 0, 0, 1, "The price for 0 tickets at $100 each with 0% sales tax and $1 processing fee is $1")
])
def test_concert_calculator(ticket_price, num_tickets, sale_tax, processing_fee, expected):
    assert concert_calculator(ticket_price, num_tickets, sale_tax, processing_fee) == expected

@pytest.mark.parametrize( "first, last, fav_word, expected", [
    ("Bruce", "Wayne", "Bat", "Mr.Bayne-3"),
    ("diana", "Prince", "Truth", "Mr.Dinca-5"),
    ("Clark", "Kent", "Flight", "Mr.Centk-6"),
    ("TONY", "stark", "Jarvis", "Mr.Ttary-6"),
    ("natasha", "romanoff", "Widow", "Mr.Nanoa-5"),
    ("peter", "PARKER", "Web", "Mr.Prker-3"),
    ("Arthur", "Cur", "Ocean", "Mr.Acurr-5"),
    ("Barry", "Allen", "", "Mr.Blley-0"),
])
def test_codename_gen(first, last, fav_word, expected):
    assert codename_gen(first, last, fav_word) == expected
