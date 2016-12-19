import pytest
import binascii
from ethereum import tester as t
from collections import namedtuple

Account = namedtuple('Account', 'address,privkey')
accounts = [Account(t.a0, t.k0),
            Account(t.a1, t.k1),
            Account(t.a2, t.k2),
            Account(t.a3, t.k3)]


def test_whitelist():
    s = t.state()
    c = s.abi_contract('whitelist.se')

    assert c.newWhitelist(sender=accounts[0].privkey) == 1
    assert c.getWhitelistCount() == 1
    assert c.getOwner(1) == binascii.hexlify(accounts[0].address)
    assert c.getDefaultWhitelist(accounts[0].address) == 1

    with pytest.raises(t.TransactionFailed):
        c.changeOwner(1, accounts[1].address, sender=accounts[1].privkey)
    assert c.changeOwner(1, accounts[1].address, sender=accounts[0].privkey) == 1
    assert c.getDefaultWhitelist(accounts[0].address) == 0

    
    with pytest.raises(t.TransactionFailed):
        c.addAddress(1, accounts[3].address, sender=accounts[0].privkey)
    assert c.addAddress(1, accounts[2].address, sender=accounts[1].privkey) == 1        
    assert c.checkWhitelist(1, accounts[2].address) == 1


    with pytest.raises(t.TransactionFailed):
        c.removeAddress(1, accounts[2].address, sender=accounts[0].privkey)
    assert c.removeAddress(1, accounts[2].address, sender=accounts[1].privkey) == 1
    assert c.checkWhitelist(1, accounts[2].address, sender=accounts[1].privkey) == 0
