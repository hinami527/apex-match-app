from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    team_data = []
    for i in range(1, 21):
        team_name = request.form.get(f'team_name_{i}', f'Team {i}')
        kills = int(request.form.get(f'kills_{i}', 0))
        placement = int(request.form.get(f'placement_{i}', 0))
        points = (21 - placement) + min(kills, 6)
        team_data.append((team_name, placement, kills, points))
    team_data.sort(key=lambda x: x[3], reverse=True)
    return render_template('results.html', team_data=team_data)

if __name__ == '__main__':
    app.run(debug=True)
