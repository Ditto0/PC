from selenium import webdriver
import  time

browser = webdriver.Chrome(executable_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
url = "http://mail.163.com/"

#打开163邮箱网页
browser.get(url)
#默认是扫码登陆，切换成密码登陆
met = browser.find_element_by_id("switchAccountLogin")
met.click()
#最大化浏览器
browser.maximize_window()
time.sleep(2)

browser.switch_to.frame(0)
#账号输入框
email=browser.find_element_by_name("email")
email.send_keys("pythonstudu@163.com")
#密码输入
passwd = browser.find_element_by_name("password")
passwd.send_keys("hennan123")
#登陆
login_em = browser.find_element_by_id("dologin")
login_em.click()
time.sleep(10)