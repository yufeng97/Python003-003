from requests import Session


url = "https://shimo.im/login?from=home"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
cookie = "shimo_gatedlaunch=6; shimo_kong=8; shimo_svc_edit=9014; _bl_uid=1jk9temqfy720Oy2nnzzomXr9hRt; _csrf=0HaNAoL35BROu7ezJGTLLSKU; deviceId=b0690022-e8d7-41ca-a8b4-0fad489a374f; deviceIdGenerateTime=1598773242601; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2237889393%22%2C%22%24device_id%22%3A%221743a067b5072-0b762f7550fe09-f7b1332-3686400-1743a067b51950%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221743a067b5072-0b762f7550fe09-f7b1332-3686400-1743a067b51950%22%7D; sensorsdata2015session=%7B%7D; anonymousUser=-10753304144; shimo_sid=s%3Ab0zqXRhIaZ36D9nSWMMbSbzc4J4kGPfi.TVQGfB2VkG%2FEI9tFgYB2dlu%2FxJvqWgTDpCQ4jzZsBkg; Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1598701338,1598773256; Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1598773257"
headers = {
    'user-agent': user_agent, 
    'referer': url,
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop',
}
data = {
    'email': 'xxxx',
    'mobile': '+86undefined',
    'password': 'xxxx'
}
session = Session()
# r = session.get(url, headers=headers)
res = session.post("https://shimo.im/lizard-api/auth/password/login", headers=headers, data=data )
print(res.status_code)
print(res.text)
