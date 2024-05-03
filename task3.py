import json
with open("data/report.json", "w") as file:
    with open("data/tests.json", "r") as file_t:
          with open("data/values.json", "r") as file_v:
            for i, j in zip(file_t.readlines(), file_v.readlines()): file.write(f"{i.strip()},{j.strip()}'\n'")