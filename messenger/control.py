########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...
class Control:
    def __init__(self, text_control, user_control, security_condition_read, security_condition_write):
        self.text_control = text_control
        self.user_control = user_control
        self.security_condition_read(text_control, user_control)
        self.security_condition_write(text_control, user_control)

    def security_condition_read(text_control, user_control):
        if text_control == "Public":
            text_control = 0
        if text_control == "Confidential":
            text_control = 1
        if text_control == "Privileged":
            text_control = 2
        if text_control == "Secret":
            text_control = 3
        return text_control <= user_control
    
    def security_condition_write(text_control, user_control):
        if text_control == "Public":
            text_control = 0
        if text_control == "Confidential":
            text_control = 1
        if text_control == "Privileged":
            text_control = 2
        if text_control == "Secret":
            text_control = 3
        return text_control > user_control