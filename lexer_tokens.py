class Token():
    def __init__(self, token_type, val=None):
        self.type = token_type
        self.val = val

    def __str__(self):
        return "Token ({}, {})".format(self.type, self.val)

    def __repr__(self):
        return self.__str__()
