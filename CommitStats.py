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

from bs4 import BeautifulSoup
import urllib.request
import re

###################################################################
# 2. FUNCTIONS
###################################################################

class User():

    """ A user object """

    def __init__(self, url):
        """ Init """
        self.url = url
        self.soup = self.make_soup()
        self.commit_list = self.get_data()
        self.total_commits = self.get_total()
        self.highest_commits = self.get_highest()
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
            number = int(re.sub("\D", "", counter.group(0)))
            commit_list.append(number)
        return commit_list


    def get_total(self):
        return sum(self.commit_list)
    def get_average(self):
        return round(self.total_commits/len(self.commit_list), 3)
    def get_highest(self):
        return max(self.commit_list)


    def print_stats(self):
        """ Print user stats """
        print("Total commits: " + str(self.total_commits))
        print("Highest commits in single day: " + str(self.highest_commits))
        print("Average commits per day: " + str(self.average_commits))


###################################################################
# 3. MAIN
###################################################################

def main():
    page = "https://github.com/NathanMH"
    git_user = User(page)
    git_user.print_stats()

main()

###################################################################
# 4. TESTING
###################################################################
