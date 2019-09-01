import yaml
with open(file="1.yaml",mode="r",encoding="utf-8") as fb:

    a = yaml.load(fb,Loader=yaml.FullLoader)
    print(a)