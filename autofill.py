from selenium import webdriver

import time

my_file = open("url_list.txt", 'r')
url_list = [""]

with open("url_list.txt") as file:
    while (line := file.readline().rstrip()):
        url_list.append(line)

print("here it is")
print(url_list)

for i in range (1, len(url_list)):
    driver = webdriver.Chrome()
    driver.get(url_list[i])

    firstName = driver.find_element_by_xpath('//*[@id="first_name"]')
    firstName.send_keys('David')

    lastName = driver.find_element_by_xpath('//*[@id="last_name"]')
    lastName.send_keys('Solinsky')

    email = driver.find_element_by_xpath('//*[@id="email"]')
    email.send_keys('dsolinsky98@gmail.com')

    phone = driver.find_element_by_xpath('//*[@id="phone"]')
    phone.send_keys('5715247794')

    #Select location

    location = driver.find_element_by_xpath('//*[@id="job_application_location"]')
    location.send_keys('Herndon, Virginia, United States')

    time.sleep(1)

    locationConfirm = driver.find_element_by_xpath('//*[@id="ui-id-1"]/li[1]')
    locationConfirm.click()

    #Upload Resume 
    #time.sleep(1)
    #upload = driver.find_element_by_xpath('//*[@id="main_fields"]/div[8]/div/div[3]/a[1]').send_keys("W:\Job Application-Resume\David_Solinsky_Resume.docx")
    #time.sleep(1)

    #Select school

    school = driver.find_element_by_xpath('//*[@id="s2id_education_school_name_0"]/a').click()
    schoolTextBox = driver.find_element_by_xpath('//*[@id="s2id_autogen6_search"]').send_keys('College of William and Mary')
    time.sleep(1)
    schoolTextBox = driver.find_element_by_xpath('//*[@id="s2id_autogen6_search"]').send_keys(u'\ue007')

    #Select degree

    degree = driver.find_element_by_xpath('//*[@id="s2id_education_degree_0"]/a').click()
    time.sleep(1)
    degreeBox = driver.find_element_by_xpath('//*[@id="select2-result-label-12"]').click()

    #Select discipline

    discipline = driver.find_element_by_xpath('//*[@id="s2id_education_discipline_0"]/a').click()
    disciplineTextBox = driver.find_element_by_xpath('//*[@id="s2id_autogen8_search"]').send_keys('Computer Science')
    time.sleep(1)
    discipline = driver.find_element_by_xpath('//*[@id="s2id_autogen8_search"]').send_keys(u'\ue007')

    #textboxes

    startMonth = driver.find_element_by_xpath('//*[@id="education_section"]/div/fieldset/div[4]/fieldset/input[1]')
    startMonth.send_keys('08')

    startYear = driver.find_element_by_xpath('//*[@id="education_section"]/div/fieldset/div[4]/fieldset/input[2]')
    startYear.send_keys('2017')

    endMonth = driver.find_element_by_xpath('//*[@id="education_section"]/div/fieldset/div[5]/fieldset/input[1]')
    endMonth.send_keys('01')

    endYear = driver.find_element_by_xpath('//*[@id="education_section"]/div/fieldset/div[5]/fieldset/input[2]')
    endYear.send_keys('2022')

    linkedIn = driver.find_element_by_xpath('//*[@id="job_application_answers_attributes_2_text_value"]')
    linkedIn.send_keys('https://www.linkedin.com/in/david-solinsky/')

    github = driver.find_element_by_xpath('//*[@id="job_application_answers_attributes_3_text_value"]')
    github.send_keys('https://github.com/dsol-cpu')


    q1 = driver.find_element_by_xpath('//*[@id="s2id_job_application_answers_attributes_4_answer_selected_options_attributes_4_question_option_id"]/a').click()
    time.sleep(1)
    q1 = driver.find_element_by_xpath('//*[@id="select2-result-label-153"]').click()

    q2 = driver.find_element_by_xpath('//*[@id="s2id_job_application_answers_attributes_5_answer_selected_options_attributes_5_question_option_id"]/a').click()
    time.sleep(1)
    q2Box = driver.find_element_by_xpath('//*[@id="select2-result-label-156"]').click()

    q3 = driver.find_element_by_xpath('//*[@id="s2id_job_application_answers_attributes_6_answer_selected_options_attributes_6_question_option_id"]/a').click()
    time.sleep(1)
    q3Box = driver.find_element_by_xpath('//*[@id="select2-result-label-168"]').click()

    q4 = driver.find_element_by_xpath('//*[@id="s2id_job_application_answers_attributes_7_answer_selected_options_attributes_7_question_option_id"]/a').click()
    time.sleep(1)
    q4Box = driver.find_element_by_xpath('//*[@id="select2-result-label-170"]').click()

    q5 = driver.find_element_by_xpath('//*[@id="s2id_job_application_answers_attributes_8_answer_selected_options_attributes_8_question_option_id"]/a').click()
    time.sleep(1)
    q5Box = driver.find_element_by_xpath('//*[@id="select2-result-label-172"]').click()

    checkBox1 = driver.find_element_by_xpath('//*[@id="demographic_questions"]/div[1]/label[1]/input').click()
    checkBox2 = driver.find_element_by_xpath('//*[@id="demographic_questions"]/div[2]/label[2]/input').click()
    checkBox3 = driver.find_element_by_xpath('//*[@id="demographic_questions"]/div[3]/label[6]/input').click()
    checkBox4 = driver.find_element_by_xpath('//*[@id="demographic_questions"]/div[4]/label[2]/input').click()