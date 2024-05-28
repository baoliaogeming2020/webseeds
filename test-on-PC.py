from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

driver_list = []
driver_numb = 3
count = 0
while ( count < driver_numb):
    driver_list.append( webdriver.Chrome() )
    count = count + 1

net_link_file = open("link.txt")
wsd_link_file = open(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())+".txt" , "w")

line = net_link_file.readline().strip('\n')

while line:
    count = 0
    num = 0
    output_line = []
    while ( count < driver_numb):
        if line:
            output_line.append(line)
            driver_list[count].get(line)
            num = num + 1
        line = net_link_file.readline().strip('\n')
        count = count + 1
    sleep(10)

    count1 = 0
    while ( count1 < num):
        element = WebDriverWait(driver_list[count1], 10).until(EC.presence_of_element_located((By.XPATH, "//button[iconpark-icon/@name='rectangle-terminal']/..")))
        element_content = element.get_attribute("innerHTML")
        lines = element_content.split('\n')
        output = output_line[count1]+"\n"+driver_list[count1].title+"\n"+lines[1][139:-2]+"\n\n"
        wsd_link_file.write(output)
        print(output)
        count1 = count1 + 1

net_link_file.close()
wsd_link_file.close()
