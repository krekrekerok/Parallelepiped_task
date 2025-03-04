from time import sleep
from utils.characteristics import calc_char
from utils.statistics import calc_stats
from utils.html import generate_html
import json
from time import sleep

pict_list = ["Parallelepiped task", "*", "*", "*\n\n"]
for i in pict_list:
    sleep(0.4)
    print(i)

with open("parallelepipeds.json", "r") as f:
    parallelepipeds_json = json.load(f)

with open("outputs/characteristics.json", "w") as file:
    json.dump(calc_char(parallelepipeds_json), file, indent=4)

with open("outputs/characteristics.json", "r") as f:
    characteristics_json = json.load(f)

with open("outputs/statistics.json", "w") as file:
    json.dump(calc_stats(characteristics_json), file, indent=4)

generate_html(calc_stats(characteristics_json))


end_ = """Created FILES
    -- outputs/characteristics.json
    -- outputs/statistics.json
    -- outputs/data_summary.html
    """
print(end_)
