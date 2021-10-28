import pandas as pd
import os
from util.constant import *

EXCEL_FILE_DIR = './Database/' + EXCEL_FILE_NAME

class User:
    def __init__(self, firstName='SampleName', lastName="SampleName", startWeight=0, endWeight=0):
        self.firstName = firstName
        self.lastName = lastName
        self.startWeight = startWeight
        self.endWeight = endWeight

    def setFirstName(self, firstName):
        self.firstName =firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setStartWeight(self, weight):
        self.startWeight = weight

    def setEndWeight(self, weight):
        self.endWeight = weight


class UserDatabase:
    def __init__(self):
        self.userDatabase = list()

        # Our software uses an excel file to store users' information
        if not os.path.exists(EXCEL_FILE_DIR):
            self.createExcelFile()
        else:
            self.initializeDatabase()

    def createExcelFile(self):
        # Use dataframe from Pandas to store titles in the first row
        df = pd.DataFrame(columns=TITLES)
        df.to_excel(EXCEL_FILE_DIR, index=False, header=True)

    def checkUserExistance(self, newUser):
        if not isinstance(newUser, User):
            #TODO: Debug Logging
            raise ValueError('New User should be an object of User')

        if len(self.userDatabase) == 0:
            return NEW_USER

        for user in self.userDatabase:
            if newUser.firstName == user.firstName and newUser.lastName == user.lastName:
                return USER_EXIST
        else:
            return NEW_USER

    def initializeDatabase(self):
        dataframe = pd.read_excel(EXCEL_FILE_DIR, sheet_name=0)

        # Get the list of users in the excel file
        userInfo = dataframe.values
        for ii in range(len(userInfo)):
            # Retrieve data from userInfo list as below
            # Index 0: First Name, index 1: Last Name, index 2: Weight before workout and index 3: weight after workout
            firstName = userInfo[ii][0]
            lastName = userInfo[ii][1]
            startWeight = userInfo[ii][2]
            endWeight = userInfo[ii][3]
            newUser = User(firstName, lastName, startWeight, endWeight)

            self.userDatabase.append(newUser)

    def addUserToDatabase(self, newUser):
        # Check if the user is in the system or not.
        userExist = self.checkUserExistance(newUser)

        if userExist == USER_EXIST:
            return userExist

        self.userDatabase.append(newUser)

        # update database
        self.updateDatabase()

        return USER_SAVED

    def getUsersList(self):
        return self.userDatabase

    def toDict(self):
        usersDict = dict()
        for title in TITLES:
            usersDict[title] = []

        for user in self.userDatabase:
            usersDict['First Name'].append(user.firstName.lower().capitalize())
            usersDict['Last Name'].append(user.lastName.lower().capitalize())
            usersDict['Weight Before Workout (lbs)'].append(user.startWeight)
            usersDict['Weight After Workout (lbs)'].append(user.endWeight)

        return usersDict

    def updateDatabase(self):
        # Update database by saving object's database to excelfile
        usersDict = self.toDict()
        df = pd.DataFrame(usersDict)
        df.to_excel(EXCEL_FILE_DIR, index=False, header=True)

    def findUserFromNames(self, firstName, lastName):
        user = next(filter(lambda u: u.firstName == firstName and u.lastName == lastName, self.userDatabase))

        if isinstance(user, User):
            return user, FOUND

        if user is None:
            return None, NOT_FOUND

    def updateUser(self, user):
        userIndex = self.userDatabase.index(user)
        self.userDatabase[userIndex] = user
        self.updateDatabase()

    def deleteUser(self, user_):
        self.userDatabase = [user for user in self.userDatabase if user is not user_]
        self.updateDatabase()
