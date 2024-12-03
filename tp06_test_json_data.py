import pytest
import json
def add(x,y):
    return x+y
def read_json_data():
    with open("user_data.json","r",encoding="utf-8") as f:
        data = json.load(f)
        result = [(item['x'],item['y'],item['expert']) for item in data]
        print(result)
    return result

data = read_json_data()

@pytest.mark.parametrize("x,y,expert",data)
class TestAddFun():
    def test_add(self,x,y,expert):
        resp = add(x,y)
        assert resp == expert

