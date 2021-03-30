
import csv as csv
import os as os
import time
import datetime
from selenium import webdriver 
from selenium.webdriver.support.select import Select

def parse_file(file):


    with open(file, newline='') as open_file:
        file_reader = csv.reader(open_file, delimiter = ',', quotechar='|')
        reader_list = list(file_reader)
        #for row in file_reader:
        #    print(row[0] + ',' + row[2] + ',' + row[3] + ',' + row[7])
    return reader_list


##file = 'C:\\Users\\scottw\\Downloads\\all_my_training.csv'
##print(file)
##parse_file(file)

def run(details: dict):
    loginId = details['id']
    loginPassword = details['password']
    session = launch_browser()
    search_box = session.find_element_by_id('cBody_btnLogin_UserName')
    search_box.send_keys(loginId)
    search_box = session.find_element_by_id('cBody_btnLogin_Password')
    search_box.send_keys(loginPassword)
    time.sleep(2)
    search_box = session.find_element_by_id('cBody_btnLogin_LoginImageButton')
    search_box.click()
    time.sleep(5)
    session.get('https://www.azaccountancy.gov/Login/My_Account/CPE%20Period.aspx')
    active_period_button = 'cBody_grdCPE_imgbtnCPEAction1_1'
    action_button = session.find_element_by_id(active_period_button)
    action_button.click()
    session.get('https://www.azaccountancy.gov/Login/My_Account/CPE.aspx')
    start_date_obj = datetime.datetime.strptime(details['date_selected'],'%m-%d-%y')
    start_date = start_date_obj.date()
    #start entering details

    details_array = parse_file(details['file'])
    for row in details_array:
        method = 'CW'
        subject = subject_switch(row[2])
        cpe_date = datetime.datetime.strptime(row[7],'%m/%d/%Y').date()
        hours = row[3].replace(';',',')
        title = row[0]
        org = 'CPExpress'

        if cpe_date < start_date:
            break

        method_button = Select(session.find_element_by_id('cBody_ddlThisCPE_Method'))
        method_button.select_by_value(method)
        time.sleep(1)

        subject_button = Select(session.find_element_by_id('cBody_ddlThisCPE_Subject'))
        subject_button.select_by_value(subject)
        time.sleep(1)

        date_button = session.find_element_by_id('cBody_dtpCPEDate_txtDate')
        date_button.send_keys(str(cpe_date))
        time.sleep(1)

        hours_button = session.find_element_by_id('cBody_txtThisCPE_FractionHours')
        hours_button.send_keys(hours)
        time.sleep(1)

        title_button = session.find_element_by_id('cBody_txtThisCPE_Title')
        title_button.send_keys(title)
        time.sleep(1)

        org_button = session.find_element_by_id('cBody_txtThisCPE_Sponsor')
        org_button.send_keys(org)
        time.sleep(1)

        intro_course_button = session.find_element_by_id('cBody_rblThisCPE_IC_1')
        intro_course_button.click()
        time.sleep(1)

        save_button = session.find_element_by_id('cBody_btnCompletedCPE')
        save_button.click()
        time.sleep(3)

    exit_button = session.find_element_by_id('cBody_btnSaveAndExit')
    exit_button.click()
    return

def launch_browser():
    driver = webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get('https://www.azaccountancy.gov/login/login.aspx');
    time.sleep(1) # Let the user actually see something!
    time.sleep(1) # Let the user actually see something!
    return driver
##driver.quit()

def subject_switch(method):
    if method == 'Accounting':
        return 'A'    
    elif method == 'Auditing':
        return 'A'
    elif method == 'Taxation':
        return 'T'
    elif method == 'Ethics':
        return 'E'
    else:
        return 'C'


      
