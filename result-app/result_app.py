from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379, db=0)

players = ["Mohamed Salah", "Ousmane Dembélé", "Lamine Yamal", "Raphinha", "Pedri", "Kylian Mbappe"]

@app.route("/")
def results():
    votes = {p: int(r.get(p) or 0) for p in players}
    total = sum(votes.values()) or 1
    html = "<h1>Ballon d'Or Voting Results</h1><ul>"
    for player in players:
        percent = (votes[player] / total) * 100
        html += f"<li>{player}: {votes[player]} votes ({percent:.1f}%)</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

