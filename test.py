from serpent_tests import ContractTest, default_accounts

A0 = default_accounts[0]
A1 = default_accounts[1]
A2 = default_accounts[2]


class WhitelistTest(ContractTest):
    source = 'whitelist.se'

    def test_newWhitelist(self):
        self.assertEqual(
            self.contract.newWhitelist(sender=A0.private_key),
            1)

    def test_getWhitelistCount(self):
        self.assertEqual(
            self.contract.getWhitelistCount(),
            1)

    def test_getOwner(self):
        self.assertEqual(
            self.contract.getOwner(1),
            A0.address)

    def test_changeOwner(self):
        with self.assertTxFail():
            self.contract.changeOwner(
                1,
                A1.address,
                sender=A1.private_key)

        self.assertTrue(
            self.contract.changeOwner(
                1,
                A1.address,
                sender=A0.private_key))

    def test_addAddress(self):
        with self.assertTxFail():
            self.contract.addAddress(
                1,
                A2.address,
                sender=A0.private_key
            )
        self.assertTrue(
            self.contract.addAddress(
                1,
                A2.address,
                sender=A1.private_key
            )
        )

    def test_checkWhitelist(self):
        self.assertTrue(
            self.contract.checkWhitelist(
                1,
                A2.address))
        self.assertFalse(
            self.contract.checkWhitelist(
                1,
                A1.address))

    def test_removeAddress(self):
        with self.assertTxFail():
            self.contract.removeAddress(
                1,
                A2.address,
                sender=A0.private_key)

        self.assertTrue(
            self.contract.removeAddress(
                1,
                A2.address,
                sender=A1.private_key))


if __name__ == '__main__':
    WhitelistTest.run_tests()


