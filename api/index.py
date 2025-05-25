import json

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    if request.method != "GET":
        return response.status(405).send("Only GET allowed.")

    names = request.query.getlist("name")
    result = []

    with open("marks.json") as f:
        data = json.load(f)
    
    # Convert list of dicts to a dict for faster lookup
    data_dict = {item["name"]: item["marks"] for item in data}

    for name in names:
        result.append(data_dict.get(name, None))  # None if name not found

    return response.json({"marks": result})
