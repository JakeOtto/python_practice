# == INSTRUCTIONS ==
#
# Purpose: Validate a password
# Parameters: one, a string
# Rules:
#   - It must be longer than 7 characters (8 is fine)
#   - It must contain at least one of the following special characters: `!`, `@`,
#     `$`, `%` or `&`
# Returns: a boolean (True if valid, False otherwise)
# Example:
#   Call:    is_valid("1234567")
#   Returns: False
#   Call:    is_valid("12345678")
#   Returns: False
#   Call:    is_valid("12345!78")
#   Returns: True

# == YOUR CODE ==

def is_valid(password):
    
    valid = False
    symbol = False 
    if len(password) <= 7:
        valid = False
        
    else:
        req_char = ["!","@","$","%","&"]
        print ("passed length")
        for i in req_char:
            if password.find(i) == -1:
                valid = False
                print ("failed search")
            else:
                symbol = True
                
    if symbol == True:
        valid = True
    return valid
