"""####################
Author: Nathan Mador-House
####################"""

#######################
"""####################
Index:
    1. Imports and Readme
    2. Functions
    3. Main
    4. Testing
####################"""
#######################

###################################################################
# 1. IMPORTS AND README
###################################################################

import re
import sys
from bs4 import BeautifulSoup
import urllib.request

###################################################################
# 2. FUNCTIONS
###################################################################

class GitUser():

    """ A user object """

    def __init__(self, url):
        """ Init """
        self.url = url
        self.soup = self.make_soup()
        self.commit_list = self.get_data()
        self.total_commits = self.get_total()
        self.best_day = self.get_best_day()
        self.best_week = self.get_best_week()
        self.best_month = self.get_best_month()
        self.average_commits = self.get_average()


    def make_soup(self):
        """ Make the html doc """
        html = urllib.request.Request(self.url)
        response = urllib.request.urlopen(html)
        html_response = response.read().decode('utf-8')
        the_soup = BeautifulSoup(html_response, 'html.parser')
        return the_soup


    def get_data(self):
        """ Get all the data for each day tag """
        commit_list = []
        days = self.soup.find_all("rect")
        for i in range(0, len(days)):
            counter = re.search('data-count="."', str(days[i]))
            commit_date = re.search('data-date=".........."', str(days[i]))
            print(commit_date)
            number = int(re.sub("\D", "", counter.group(0)))
            commit_list.append(number)
        return commit_list


    def get_total(self):
        return sum(self.commit_list)
    def get_average(self):
        return round(self.total_commits/len(self.commit_list), 3)
    def get_best_day(self):
        return max(self.commit_list)
    def get_best_month(self):
        pass
    def get_best_week(self):
        pass


    def print_stats(self):
        """ Print user stats """
        print("Total commits: " + str(self.total_commits))
        print("Highest commits in single day: " + str(self.highest_commits))
        print("Average commits per day: " + str(self.average_commits))


###################################################################
# 3. MAIN
###################################################################

def main():
    page = str(sys.argv[1])
    git_user = GitUser(page)
    git_user.print_stats()

#main()

###################################################################
# 4. TESTING
###################################################################

def test():
    page = "https://github.com/NathanMH"
    git_user = User(page)

test()

