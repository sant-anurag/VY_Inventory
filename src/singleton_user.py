class CurrentUser:
    __instance__ = None

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance."""
        if not CurrentUser.__instance__:
            CurrentUser()
        return CurrentUser.__instance__

    def __init__(self):
        """ Constructor."""
        self.currentUserName = ''
        if CurrentUser.__instance__ is None:
            CurrentUser.__instance__ = self
        else:
            raise Exception("You cannot create another CurrentUser class")

    def setCurrentUser(self, username):
        print("Current user is set as :", username)
        self.currentUserName = username

    def getCurrentUser(self):
        return self.currentUserName
