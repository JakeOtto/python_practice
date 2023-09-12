# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#   4. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# We recommend that you store the passwords in a dictionary, where the keys are
# the service names and the values are the passwords.
#
# Example usage:
#   > password_manager = PasswordManager()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.get_for_service('not_real')
#   None
#   > password_manager.get_for_service('twitter')
#   None
#   > password_manager.list_services()
#   ['gmail', 'facebook']
#

# == YOUR CODE ==

class PasswordManager():

    def __init__(self):
        self.password_dic = {}
        
    def add(self, ser_name, ser_pass):
        
        valid = False
        req_char = ["!", "@", "$", "%", "&"]

        if len(ser_pass) >= 8 and any (char in ser_pass for char in req_char):
            valid = True

        if valid:
            self.password_dic[ser_name]=ser_pass

    def get_for_service(self, ser_name):
        
        for key, value in self.password_dic.items():
            if key == ser_name:
                return value
            
        return None
    
    def list_services(self):
        keys_list = []
        for key, value in self.password_dic.items():
            if value != None:
                keys_list.append(key)

        return keys_list
