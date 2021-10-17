import json
import pandas as pd

final_data={"data":[]}


def get_data_and_create_node(datafile="data.csv"):
    data=pd.read_csv(datafile,encoding="iso8859_1",sep=";",keep_default_na=False)

    for idx,element in data.iterrows():
    #  if element["topic"]=="Vaccination": #test only
            res={}
            
        #  print(element["topic"])

            res["criteria_id"]=element["criteria_id"]
            res["criteria_title"]=element["criteria_title"]
            res["criteria_status"]=element["criteria_status"]
            res["criteria_link"]=element["criteria_link"]
            res["intervention_id"]=element["intervention_id"]
            res["intervention_nr"]=element["intervention_nr"]
            res["intervention_title"]=element["intervention_title"]

    final_data["data"]=data.to_dict(orient="records")
    with open("data/data.json", "w") as fout:
        json.dump(final_data, fout)

get_data_and_create_node()

