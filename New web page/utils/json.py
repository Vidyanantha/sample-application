import json

def read_json(file):
    rj=open(file,"read")
    json_data=json.load(rj)
    rj.close()
    return json_data


def write_json(file,data):
    wj=open(file,"w")
    json_data=json.dumps(data,indent=4)
    wj.write(json_data) 
    wj.close()


def fix_id(data):
    i=1
    for task in data:
        task["id"]=i
        i+=1
    return data        

    