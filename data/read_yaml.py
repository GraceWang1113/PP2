import yaml
import json


a = yaml.load(open("demo.yml",encoding='utf-8'),Loader=yaml.FullLoader)
print(a)
json_a=json.dumps(a,indent=5)
print(json_a)