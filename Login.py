import requests

session = requests.Session()
session.get(url = "https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.19213366492054385")
resp = session.post(url = "https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.6678262295913706",
             data={"username":"13800000002","password":"123456","verify_code":"8888"})
print("登陆结果",resp.json())


