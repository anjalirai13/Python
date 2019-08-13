from selenium import webdriver
 browser = webdriver.Chrome()
 browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
 browser.find_element_by_id('user-message').send_keys("Hello")
 browser.find_element_by_class_name('btn-default').click()
browser.find_element_by_class_name('btn-default').click()
 browser.find_element_by_id('user-message').send_keys("This is a cool test")
 browser.find_element_by_class_name('btn-default').click()
 browser.find_element_by_id('user-message').clear()
 browser.find_element_by_id('user-message').send_keys("This is a cool test")
 browser.find_element_by_class_name('btn-default').click()

 browser.find_element_by_id('display').text
'This is a cool test'

 browser.find_element_by_id('sum2').send_keys(4)
 browser.find_element_by_id('sum2').clear()
 browser.find_element_by_id('sum2').send_keys(4)
 browser.find_element_by_id('sum1').send_keys(3)
 browser.find_element_by_id('sum2').send_keys(2)
browser.find_element_by_xpath('//*[@id="gettotal"]/button').click()
 browser.find_element_by_id('displayvalue').text
'7'
browser.find_element_by_xpath('//button[text()="Get Total"]').click()
submit_button = browser.find_element_by_xpath('//*[@id="gettotal"]/button')
 submit_button.click()

browser.find_element_by_link_text('Input Forms').click()
 browser.find_element_by_link_text('Simple Form Demo').click()
 browser.find_element_by_link_text('Input Forms').click()
 browser.find_element_by_link_text('Checkbox Demo').click()
 browser.find_element_by_id('isAgeSelected').click()
 browser.find_element_by_id('txtAge').text()	

browser.find_element_by_xpath("//button[text()='Get values']").click()
 browser.find_element_by_class_name('groupradiobutton').text
'Sex : Female\nAge group: 15 - 50'
 browser.find_element_by_link_text('Input Forms').click()
 browser.find_element_by_link_text('Select Dropdown List').click()

 browser.maximize_window()
 browser.find_element_by_link_text('Input Forms').click()
 browser.find_element_by_link_text('Radio Buttons Demo').click()
 browser.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/label[1]/input').click()
 browser.find_element_by_id('buttoncheck').click()
 browser.find_element_by_class_name('radiobutton').text
"Radio button 'Male' is checked"
 browser.find_element_by_xpath("//input[@name='gender' and @value='Female']").click()

 browser.find_element_by_xpath("//input[@name='ageGroup' and @value='15 - 50']").click()



browser.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[3]/label/input').click()

browser.find_element_by_id('check1').click()
browser.find_element_by_id('check1').text
