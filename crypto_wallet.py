# Cryptocurrency Wallet
################################################################################

# This file contains the Ethereum transaction functions that you have created throughout this module’s lessons.
# By using import statements, you will integrate this `crypto_wallet.py` Python script
# into the KryptoJobs2Go interface program that is found in the `krypto_jobs.py` file.

################################################################################
# Imports
import os
import requests
from dotenv import load_dotenv

load_dotenv('Sample.env')
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

################################################################################
# Wallet functionality


def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from environment variable.
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet Object
    wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)

    return account


def get_balance(w3, address):
    """Using an Ethereum account address access the balance of Ether"""
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)

    # Convert Wei value to ether
    ether = w3.fromWei(wei_balance, "ether")

    # Return the value in ether
    return ether


def send_transaction(w3, account, to, wage):
    """Send an authorized transaction to the Ganache blockchain."""
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert eth amount to Wei
    value = w3.toWei(wage, "ether")

    # Set a fixed gas price
    gas_price = w3.toWei(10, "gwei")  # 10 Gwei

    # Calculate gas estimate
    gasEstimate = w3.eth.estimateGas(
        {"to": to, "from": account.address, "value": value}
    )

def send_transaction(w3, account, to, wage):
    """Send an authorized transaction to the Ganache blockchain."""
    # Convert eth amount to Wei
    value = w3.toWei(wage, "ether")
    
    # Set a fixed gas price
    gas_price = w3.toWei(10, "gwei")  # 10 Gwei
    
    # Calculate gas estimate
    gas_estimate = w3.eth.estimate_gas({"to": to, "from": account.address, "value": value})
    
    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gas_estimate,
        "gasPrice": gas_price,
        "nonce": w3.eth.get_transaction_count(account.address)
    }
    
    # Sign the raw transaction with the Ethereum account
    signed_tx = account.sign_transaction(raw_tx)
    
    # Send the signed transaction
    return w3.eth.send_raw_transaction(signed_tx.rawTransaction)
