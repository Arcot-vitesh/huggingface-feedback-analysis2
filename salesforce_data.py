from simple_salesforce import Salesforce

def connect_salesforce():
    sf = Salesforce(
        username="your_salesforce_username",
        password="your_salesforce_password",
        security_token="your_security_token"
    )
    return sf
