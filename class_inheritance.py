class Califonia: #This is the parent class
    name = 'No name provided'
    county = 'Marin'
    town = 'San Anselmo'
    county_code = 1234


class Voting(Califonia): #first Child class as "voting"
    registered_to_vote = 'yes' #attributes of first child class
    age = 27

class RV(California): #second child class as "Reg voters"
    mailing_address = ' ' #attributes of first child class
    mailing_list =True
    
    
    
