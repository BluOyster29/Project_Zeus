from tdm.lib.device import DddDevice, DeviceWHQuery
from funkshons import clean_account_details


class MonzoDevice(DddDevice):

    class account_details(DeviceWHQuery):
        '''This function checks the users balance and requires'''
        def perform(self, select_account):
            endpoint = self.device.API_ENDPOINTS.get(ACCOUNTS)
            header = self.device.HEADERS
            response = clean_account_details(requests.get(endpoint, headers=headers).json())
            return response

CURRENT = "user_00009Z2sSGIUDzcXctzkcD"
BALANCE = "balance"
TRANSACTIONS = "transactions"
POTS = "pots"
HEADERS = {"Authorization" : "Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJlYiI6IlFXUi93TER6QlVYZGs2Vk5iNTZ3IiwianRpIjoiYWNjdG9rXzAwMDA5b2E3bU81bFlla0wyTldlM3QiLCJ0eXAiOiJhdCIsInYiOiI2In0.nd2c5dnhCOrWgPMOycHsWMaIaHnpq6DUpmvo9QJ6fCTjPjrytKT8v09PripFNZFtBXTwHlRTxcdRUZ3Do-sgeA"}
ACCOUNT_ID = "user_00009Z2sSGIUDzcXctzkcD"
POT_ID = "pot_00009cj4TafFU2lqI95qR0"
API_ENDPOINTS = {BALANCE     : "https://api.monzo.com/balance",
                 #Shows the user their acount balance
                 ACCOUNTS    : "https://api.monzo.com/accounts",
                 #Shows the user account information
                 TRANSACTIONS : "https://api.monzo.com/transactions",
                 #Shows the user their transactions
                 POTS        : "https://api.monzo.com/pots"}
                 #Shows users pot
