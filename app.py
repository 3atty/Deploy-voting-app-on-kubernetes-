from flask import Flask, render_template, request, redirect
import redis

app = Flask(__name__)
r = redis.Redis(host="redis-service", port=6379, db=0)

players = ["Mohamed Salah", "Ousmane Dembélé", "Lamine Yamal", "Raphinha", "Pedri", "Kylian Mbappe"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        player = request.form["player"]
        r.incr(player)
        return redirect("/")
    votes = {p: int(r.get(p) or 0) for p in players}
    return """
    <h1>Ballon d'Or Voting</h1>
    <form method="POST">
    """ + "".join([f'<input type="radio" name="player" value="{p}"> {p}<br>' for p in players]) + """
    <input type="submit" value="Vote">
    </form>
    <h2>Current Votes</h2>
    """ + "<br>".join([f"{p}: {votes[p]}" for p in players])

# ✅ هذا هو الجزء المهم جدًا:
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

