import threading
from selenium import webdriver
import time


info_set = set()


def parse_city_jobs(city, num):
    city_dict = {
        "shenzhen": "深圳",
        "shanghai": "上海",
        "beijing": "北京",
        "guangzhou": "广州",
    }
    browser = webdriver.Chrome()
    global info_set
    for i in range(1, num + 1):
        try:
            browser.get("http://lagou.com/{}-zhaopin/Python/{}/".format(city, i))
            job_money = browser.find_elements_by_xpath('//span[@class="money"]')
            job_names = browser.find_elements_by_xpath('//h3')
            names = [name.text.strip() for name in job_names]
            salaries = [salary.text.strip() for salary in job_money]
        except Exception as e:
            print(e)
        for j in range(len(names)):
            info = '{}_{}_{}'.format(city_dict[city], names[j], salaries[j])
            info_set.add(info)
        time.sleep(1)
    browser.close()
    return info_set


def main():
    cities = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
    tasks = [threading.Thread(target=parse_city_jobs, args=(city, 10,)) for city in cities]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
    with open("./jobs.txt", "w", encoding='utf8') as f:
        for info in info_set:
            f.write("{}\n".format(info))
    print(info_set)


if __name__ == "__main__":
    main()
