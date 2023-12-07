import pandas as pd
import os
import json


def read_json(file_path):
    file = open(file_path, "r")
    return json.load(file)


def read_all_json_files(JSON_ROOT):
    my_list = []

    for name in os.listdir(JSON_ROOT):
        path = os.path.join(JSON_ROOT, name)

        if os.path.isfile(path):
            my_list.append(read_json(path))
    return my_list


def read_all_json_files(JSON_ROOT):
    df = pd.DataFrame()

    for name in os.listdir(JSON_ROOT):
        path = os.path.join(JSON_ROOT, name)
        file = open(path, "r")
        json_content = json.load(file)
        df1 = pd.DataFrame(json_content["results"])
        # df1['source'] = name
        df = pd.concat([df1, df])

    df.reset_index(inplace=True)
    df = df.drop(columns=['index'], axis=1)

    return df

# df = read_all_json_files('data/daily_summaries')
# print(df)

