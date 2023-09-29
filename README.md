
<img width="584" alt="Screenshot 2023-09-28 at 11 05 17 PM" src="https://github.com/P4RASTOO/Challenge_19/assets/132952512/0dc013a0-c05f-4f75-a6b9-3b5b45bf1cf8">

# Challenge_18 Report
## Overview of the Analysis:
The analysis represents a cryptocurrency wallet application designed for KryptoJobs2Go customers. It allows users to perform various tasks related to Ethereum transactions, including creating an Ethereum account, checking the account balance, calculating the total value of a transaction, digitally signing a transaction, and reviewing transaction details on the Ganache blockchain. A breakdown the stages of process include:

1)   Importing Ethereum Transaction Functions: In this stage, the code imports necessary functions from the crypto_wallet.py script to facilitate Ethereum wallet operations. These functions include generating an Ethereum account, checking the account balance, and sending transactions.
2)   KryptoJobs2Go Candidate Information: This stage initializes a database of KryptoJobs2Go candidates, including their names, Ethereum addresses, ratings, and hourly costs per Ether. It also creates a Streamlit interface for displaying candidate information to users.
3)   Streamlit Application: The Streamlit application's main functionality is implemented in this stage. Users interact with the application to select a candidate, specify the number of hours worked, and initiate a payment transaction to the selected candidate. The application calculates the total wage, sends the transaction, and displays the transaction hash.
4)   Inspect the Transaction: This stage involves using the Streamlit application to send a test transaction, and then users can inspect the resulting transaction hash in Ganache for validation.

## Methods Used:
### Blockchain Transactions:
The code leverages Web3.py to interact with the Ethereum blockchain. It allows users to create accounts, check balances, estimate gas, and send signed transactions.
### Streamlit Interface: 
The application's user interface is built using Streamlit, making it easy for users to interact with the blockchain functions.

## Summary:
The application provides a user-friendly interface for interacting with Ethereum blockchain transactions. Users can hire KryptoJobs2Go candidates, calculate payments in Ether, and initiate payments securely. It also integrates with the Ganache blockchain for transaction validation.

## Recommendation:
To Improve User Instructions: We may nclude clear and concise instructions within the application to guide users through the process of hiring candidates and sending transactions.
For Gas Price Optimization: We can consider implementing dynamic gas price estimation to ensure that transactions are processed efficiently on the Ethereum network.
Overall, the cryptocurrency wallet application serves as a valuable tool for KryptoJobs2Go customers to manage their Ethereum transactions effectively.

###Demo of App, left side start up/app demo and right side Ganache accounts are displayed:
https://github.com/P4RASTOO/Challenge_19/assets/132952512/713428a8-abe9-47c7-930a-9f30c28e35ae




### Transactions on Ganache:
<img width="1062" alt="Screenshot 2023-09-28 at 11 48 32 PM" src="https://github.com/P4RASTOO/Challenge_19/assets/132952512/dfd45aab-8d8f-420a-bd61-8b4aeb097f21">
