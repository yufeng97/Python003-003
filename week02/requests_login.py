from requests import Session


url = "https://shimo.im/login?from=home"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
cookie = "shimo_gatedlaunch=6; shimo_kong=8; shimo_svc_edit=9014; _csrf=AMHjUwoGW-BaJV0XrK1tUpYl; deviceId=6f25050d-2d81-4d66-a887-d95a8a0d5d9e; deviceIdGenerateTime=1598670184486; sensorsdata2015session=%7B%7D; _bl_uid=1jk9temqfy720Oy2nnzzomXr9hRt; sajssdk_2015_cross_new_user=1; Hm_lvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1598701338; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2237889393%22%2C%22%24device_id%22%3A%221743a067b5072-0b762f7550fe09-f7b1332-3686400-1743a067b51950%22%2C%22props%22%3A%7B%7D%2C%22first_id%22%3A%221743a067b5072-0b762f7550fe09-f7b1332-3686400-1743a067b51950%22%7D; anonymousUser=-10722915378; shimo_sid=s%3AG3P8zLsnA4I1nofRBB-vLH4kyohRohmQ.GRXoLjDee6h3WGOq9L%2BlpVBLaS9m3dQXTvkReVaDheU; Hm_lpvt_aa63454d48fc9cc8b5bc33dbd7f35f69=1598701830"
headers = {
    'user-agent': user_agent, 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
data = {
    'email': 'xxxxxx',
    'mobile': '+86undefined',
    'password': 'xxxxxx'
}
session = Session()
r = session.get(url, headers=headers)
res = session.post("https://shimo.im/lizard-api/auth/password/login", headers=headers, data=data)
print(res.text)
