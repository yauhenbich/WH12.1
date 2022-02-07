import json


def get_candidates():
    with open('data/candidates.json', 'r', encoding="utf-8") as fp:
        candidates = json.load(fp)

    return candidates


def load_settings():
    with open('data/settings.json', 'r', encoding="utf-8") as fp:
        settings = json.load(fp)

    return settings


def get_candidate_by_id(c_id):
    candidates = get_candidates()
    for candidate in candidates:
        if c_id == candidate.get("id"):

            return candidate


def get_candidate_by_name(name):
    candidates = get_candidates()
    settings = load_settings()
    candidates_new = []

    for candidate in candidates:
        if _make_search(name, candidate['name'], settings['case-sensitive']):
           candidates_new.append(candidate)

    return candidates_new


def get_candidate_by_skill(skill_name):
    candidates = get_candidates()
    settings = load_settings()
    candidates_new = []

    for candidate in candidates:
        if _make_search(skill_name, candidate['skills'], settings['case-sensitive']):
           candidates_new.append(candidate)

    limit = settings["limit"]
    candidates_new = candidates_new[:limit]

    return candidates_new


def _make_search(search_for, user_name, case_sensitive):

    if case_sensitive:
        if search_for in user_name:
            return True
    else:
        if search_for.lower() in user_name.lower():
            return True

    return False