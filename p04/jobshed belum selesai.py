from emosi import Emosi

def test_emosi_senang():
    e = Emosi(0.8)
    assert e.tentukan_label() == "senang"

def test_emosi_sedih():
    e = Emosi(0.2)
    assert e.tentukan_label() == "sedih"

def test_emosi_netral():
    e = Emosi(0.5)
    assert e.tentukan_label() == "netral"