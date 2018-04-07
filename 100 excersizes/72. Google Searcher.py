# Create a script that let the user type in a search term and opens and search it in google
#
# from selenium import webdriver
# import time
#
# user_input = input('What you would like to search in google')
#
# browser = webdriver.Chrome()
# browser.get(url='http://www.google.com')
# time.sleep(3)
# searchbox = browser.find_element_by_id('lst-ib')
# searchbox.click()
# searchbox.send_keys(user_input)
# logo = browser.find_element_by_id('hplogo')
# logo.click()
# searchaction = browser.find_element_by_name('btnK')
# searchaction.click()
#

# from Udemy


import webbrowser

query = input("Enter your Google query: ")
url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % query
webbrowser.open_new(url)