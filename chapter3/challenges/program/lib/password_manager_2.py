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
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime
class PasswordManager2():
    
    # constructor - self  
    def __init__(self):
        self.password_dict = {}

    # add  - self, ser_name, ser_pass
    def add(self,ser_name,ser_pass):
        time = datetime.today()
        valid = False
        req_char = ["!","@","$","%","&"]
    
        if len(ser_pass) >= 8 and any (char in ser_pass for char in req_char):
            if bool(self.password_dict) == False:
                valid = True

            else:
                password_list=[]
                for info in self.password_dict.values():
                    password_list.append(info["password"])
                    if ser_pass not in password_list:
                        valid = True
            
        if valid:
            self.password_dict[ser_name]={}
            self.password_dict[ser_name]["password"]=ser_pass
            self.password_dict[ser_name]["added_on"]=time

    # remove  - self, ser_name
    def remove(self, ser_name):
        del self.password_dict[ser_name]

    # update - self, ser_name
    def update(self, ser_name,ser_pass):
        time = datetime.today()
        valid = False
        req_char = ["!","@","$","%","&"]
    
        if len(ser_pass) >= 8 and any (char in ser_pass for char in req_char):
            if bool(self.password_dict) == False:
                valid = True

            else:
                password_list=[]
                for info in self.password_dict.values():
                    password_list.append(info["password"])
                if ser_pass not in password_list:
                    valid = True
            
        if valid:
            self.password_dict[ser_name]={}
            self.password_dict[ser_name]["password"]=ser_pass
            self.password_dict[ser_name]["added_on"]=time

    # list services - self
    def list_services(self):
        keys_list=[]
        for key, value in self.password_dict.items():
            if value != None:
                keys_list.append(key)
        return keys_list

    # get for service - self , ser_name
    def get_for_service(self, ser_name):
        for key, value in self.password_dict.items():
            if key == ser_name:
                return self.password_dict[ser_name]["password"]
        else:
            return None
        

    # sort services  - self, *args
    def sort_services_by(self,*args):
        if args == "service" or args == ('service',):
            return sorted(self.password_dict)
        
        elif args == ("service", "reverse"):
            sorted_list = sorted(self.password_dict)
            sorted_list.reverse()
            return sorted_list
        
        elif args == "added_on" or args == ('added_on',):
            sorted_tuple_list = sorted(self.password_dict.items(), key = lambda x: x[1]["added_on"])
            sorted_key_list = []
            for i in sorted_tuple_list:
                sorted_key_list.append(i[0])
            return sorted_key_list
            
        elif args == ("added_on", "reverse"):
            sorted_tuple_list = sorted(self.password_dict.items(), key = lambda x: x[1]["added_on"])
            sorted_key_list = []
            for i in sorted_tuple_list:
                sorted_key_list.append(i[0])
            sorted_key_list.reverse()
            return sorted_key_list
        

#git checkin