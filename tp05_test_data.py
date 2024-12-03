import pytest
import json
def add(x,y):
    return x+y
def read_json_data():
    with open("user_data.json","r","ultr-8") as f:
        json.data = json.load(f)
        result = [(item['x'],item['y'],item['expert']) for item in json.data]
        print(result)
    return result
data = read_json_data()
#data = [(10,20,30),(100,200,300),(120,150,270)]
@pytest.mark.parametrize("x,y,expert",data)

class TestAddFun():
    def test_add(self,x,y,expert):
        resp = add(x,y)
        assert resp == expert
#    def test_add_02(self):
#        resp = add(100,200)
#        assert  resp == 300
#    def test_add_03(self):
#        resp = add(120,150)
#        assert resp == 270

