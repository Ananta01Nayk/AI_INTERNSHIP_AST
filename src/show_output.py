from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json

app = FastAPI()


def load_data():
    with open("entities.json", "r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/", response_class=HTMLResponse)
def home():
    data = load_data()

    html = """
    <html>
    <head>
        <title>ai code intelligence</title>
        <style>
            body { font-family: Arial; background:#f5f5f5; padding:20px; }
            .card { background:white; padding:15px; margin:10px; border-radius:8px; box-shadow:0 0 5px #ccc; }
            pre { background:#111; color:#0f0; padding:10px; overflow:auto; }
        </style>
    </head>
    <body>
    <h1>ai code intelligence dashboard</h1>
    """

    for section in ["functions", "classes", "variables"]:
        html += f"<h2>{section}</h2>"

        for key, info in data[section].items():
            html += f"""
            <div class="card">
                <b>{info["name"]}</b><br>
                <small>{info["file"]}</small>
            """

            if "function_code" in info:
                html += f"<pre>{info['function_code']}</pre>"

            if "class_code" in info:
                html += f"<pre>{info['class_code']}</pre>"

            html += "</div>"

    html += "</body></html>"
    return html
