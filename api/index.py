import json

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    if request.method != "GET":
        return response.status(405).send("Only GET allowed.")

    names = request.query.getlist("name")

    with open("marks.json") as f:
        data = json.load(f)

    data_dict = {d["name"]: d["marks"] for d in data}
    result = [data_dict.get(n, None) for n in names]

    return response.json({"marks": result})
