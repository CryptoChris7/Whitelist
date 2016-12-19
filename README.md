# Whitelist
### A whitelist contract for Ethereum Dapps.

## Motivation
Ethereum is a cryptocurrency with the ability to execute smart contracts, or arbitary code running on a virtual machine triggered by a transaction.
These smart contracts are limited in size, so for complex applications, it is neccessary to split code into several contracts. It may be that case
that these individual contracts need to be able to modify each other's state in a way that isn't accessible to other contracts or people who use
the Ethereum network. This contract aims to provide a simple mechanism for keeping track of groups of addresses which are allowed to access these
priviledged functions.

## Mechanism
A whitelist is a set of addresses which are allowed to access important functions in a group of smart contracts. In this smart contract, a
whitelist is uniquely identified with a uint96 value I. These values start with 1, and increment with every newly created whitelist. When a
whitelist is created, the global count of whitelists is incremented, the sender's address A is stored at the storage index I, and I is stored
at the storage index A. Storing A at index I is how the owner of whitelist I is kept track of, which allows for simple verification before mutating
whitelists, and also allows ownership transfers in the event of contract upgradaes. Storing I at index A allows for keeping track
of a default whitelist for convenience. Anyone may change their default whitelist to any whitelist which they own. Anyone can transfer ownership of
a whitelist which they own to anyone else. This allows for contracts to transfer ownership to updated version of themselves.

## Functions
Documentation of the functions is coming soon. For now, just look at the code! ;)

## Tests
To run the tests, do `py.test test.py`