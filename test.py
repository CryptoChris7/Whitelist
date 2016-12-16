import pytest
import binascii
from ethereum import tester as t


def test_whitelist():
    s = t.state()
    c = s.abi_contract('whitelist.se')

    assert c.newWhitelist() == 1
    assert c.newWhitelist(sender=t.k1) == 2
    assert c.getWhitelistCount() == 2
    assert c.getOwner(1) == binascii.hexlify(t.a0)
    assert c.getOwner(2) == binascii.hexlify(t.a1)
    assert c.getDefaultWhitelist(t.a0) == 1
    assert c.getDefaultWhitelist(t.a1) == 2

    with pytest.raises(t.TransactionFailed):
        c.changeOwner(2, t.a2, sender=t.k0)

    assert c.changeOwner(2, t.a2, sender=t.k1) == 1
    assert c.getDefaultWhitelist(t.a1) == 0
    assert c.changeDefault(2, sender=t.k2) == 1
    assert c.getDefaultWhitelist(t.a2) == 2

    assert c.addAddress(1, t.a3) == 1
    with pytest.raises(t.TransactionFailed):
        c.addAddress(1, t.a4, sender=t.k1)
        
    assert c.checkWhitelist(1, t.a3) == 1
    assert c.checkWhitelist(1, t.a4) == 0

    with pytest.raises(t.TransactionFailed):
        c.removeAddress(1, t.a3, sender=t.k1)
    
    assert c.removeAddress(1, t.a3) == 1
    assert c.checkWhitelist(1, t.a3) == 0
