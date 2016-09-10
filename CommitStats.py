#!/usr/bin/env python

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

###################################################################
# 2. FUNCTIONS
###################################################################


def make_html(url):
    html = urllib.request.Request(url)
    response = urllib.request.urlopen(html)
    return response.read().decode('utf-8')


def make_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_all_days(soup):
    days = soup.find_all("rect", class_="day")
    print("hi")
    print(days)
    print("bye")
    return days

def 

###################################################################
# 3. MAIN
###################################################################

###################################################################
# 4. TESTING
###################################################################

site = "https://github.com/NathanMH"
html = make_html(site)
soup = make_soup(html)
days = get_all_days(soup)
