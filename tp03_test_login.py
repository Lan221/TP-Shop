import requests
from py02_TPShopAPI import TPShopAPI

class Test_TPshopLogin:
    session = None
    def setup_method(self):
        self.session = requests.session()
        TPShopAPI.verify_code(self.session)

    def test_login_success(self):

        login_data = {
                       "username": "13800000002",
                       "password": "123456",
                        "verify_code": "8888"
                        }
        response = TPShopAPI.login(self.session, login_data)
        print("登陆成功", response.json())
        assert 200 == response.status_code
        assert "登陆成功" in response.json().get("msg")
        assert 1 == response.json().get("status")

   # def test_login_password_error(self):

    #    login_data = {"username": "13800000002", "password": "123457", "verify_code": "8888"}
     #  print("密码错误", response.json())
    #    assert 200 == response.status_code
    #    assert "密码错误" in response.json().get("msg")
    #    assert -2 == response.json().get("status")



