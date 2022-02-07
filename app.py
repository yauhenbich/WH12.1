from flask import Flask, render_template, request
from utils import get_candidates, load_settings, get_candidate_by_id, get_candidate_by_name, get_candidate_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    settings = load_settings()
    online = settings.get("online")
    if online:
        return "Приложение работает"
    return "Приложение не работает"


@app.route('/candidate/<int:c_id>/')
def page_candidate(c_id):
    candidate = get_candidate_by_id(c_id)
    return render_template("candidate.html", candidate=candidate)


@app.route('/list/')
def page_candidates_list():
    candidates = get_candidates()
    return render_template("list.html", candidates=candidates)


@app.route('/search')
def page_search_by_name():
    name = request.args['name']
    candidates = get_candidate_by_name(name)
    candidates_count = len(candidates)
    return render_template("search.html", candidates=candidates, candidates_count=candidates_count)


@app.route('/skill/<skill_name>')
def page_search_by_skill(skill_name):
    candidates = get_candidate_by_skill(skill_name)
    candidates_count = len(candidates)
    return render_template("skill.html", candidates=candidates, candidates_count=candidates_count,
                           skill_name=skill_name)


app.run()
