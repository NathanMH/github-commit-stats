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


def make_html(url):
    """ Make the html doc """
    html = urllib.request.Request(url)
    response = urllib.request.urlopen(html)
    return response.read().decode('utf-8')


def make_soup(html):
    """ Make the soup """
    the_soup = BeautifulSoup(html, 'html.parser')
    return the_soup


def get_total_commits(soup):
    """ Get the easy number """
    total = soup.find_all("h3")
    return re.sub("\D", "", total[1].string)


def get_all_days(soup):
    """ Get all the data for each day tag """
    date_count = []
    days = soup.find_all("rect")
    for i in range(0, len(days)):
        counter = re.search('data-count="."', str(days[i]))
        number = int(re.sub("\D", "", counter.group(0)))
        date_count.append(number)
    return date_count


def count_math(count_list):
    total = sum(count_list)
    average = round(total/len(count_list), 3)
    highest = max(count_list)
    print("Total commits: " + str(total))
    print("Highest commits in single day: " + str(highest))
    print("Average commits per day: " + str(average))

###################################################################
# 3. MAIN
###################################################################

# print(get_total_commits(soup))

###################################################################
# 4. TESTING
###################################################################

def test():
    """ Test function """
    site = "https://github.com/NathanMH"
    html = make_html(site)
    soup = make_soup(html)
    date_count = get_all_days(soup)
    count_math(date_count)

test()
