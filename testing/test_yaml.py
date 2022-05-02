import yaml
# pip install pyyaml

def test_yaml():
    # safe_load：把yaml 格式 转成python对象
    # safe_dump：把转成python对象 转成yaml格式
    with open("./demo.yaml", encoding="utf-8") as f:
        result = yaml.safe_load(f)

        print(result)