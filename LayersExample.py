# Sample script representing Layered Software Architecture based on blog:
# http://fewagainstmany.com/blog/introduction-to-layered-architecture-part-one

USERS = {"bsmith":{"firstname":"Brian", "lastname":"Smith"},
         "jdoe":{"firstname":"John", "lastname":"Doe"}
         }


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class UserDAO:
    def __init__(self):
        pass

    def retrieve(self, userID):
        self.userID = userID
        firstname = USERS[self.userID]["firstname"]
        lastname = USERS[self.userID]["lastname"]

        userFromPersistentLayer = User(firstname, lastname)
        return userFromPersistentLayer

    def create(self, userID, firstname, lastname):
        USERS.update({userID:{'firstname':firstname, 'lastname':lastname}})

    def delete(self,userID):
        del USERS[userID]

class UserManager:
    def __init__(self):
        self.dao = UserDAO()

    def retrieve(self, userID):
        userRetrieved = self.dao.retrieve(userID)
        return userRetrieved


myDAO = UserDAO()
user = myDAO.retrieve("bsmith")
print user.lastname, user.firstname
myDAO.create('bgate', 'Bill', 'Gates')
user = myDAO.retrieve('bgate')
print user.lastname, user.firstname
print "------------"
user = UserManager()
uretrieved = user.retrieve('bsmith')
print uretrieved.firstname, uretrieved.lastname
