
import requests
class TPShopAPI:
    @classmethod
    def verify_code(cls,session):
        session.get(url = "https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.19213366492054385")

    @classmethod
    def login(cls,session,login_data):
        resp = session.post(url = "https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.6678262295913706",
             data=login_data)
        return resp

