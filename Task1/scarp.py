import re 
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
test_links = open('links.txt', 'r') 
url = test_links.readlines()
file1 = open('results.txt', 'w') 
for link in url:
    file1.writelines(link)
    driver.get(link)
    html = driver.page_source

    ipv4_pattern = re.compile(r'(?:^|\b(?<!\.))(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])') 
    ipv6_pattern = re.compile(r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))')

    ipv4_list = ipv4_pattern.findall(html)
    ipv6_list = ipv6_pattern.findall(html)
    ip_value = [] 
    
    def check(pattern,Ip):  
        if(re.search(pattern, Ip)):  
            return True           
        else:  
            return False 

    if ipv4_list:
        for i in ipv4_list: 
            if i not in ip_value: 
                ip_value.append(i)

        for line in range(len(ip_value)):
            val1 = check(ipv4_pattern,ip_value[line])
            if val1:
                file1.writelines(ip_value[line]) 
                file1.writelines("\n")

    elif ipv6_list:
        for i in ipv6_list: 
            if i not in ip_value: 
                ip_value.append(i)

        for line in range(len(ip_value)):
            val1 = check(ipv6_pattern,ip_value[line][0])
            if val1:
                file1.writelines(ip_value[line][0]) 
                file1.writelines("\n")
    file1.writelines("\n\n")
file1.close()
driver.quit()
print("Success...")

