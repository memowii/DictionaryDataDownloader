import flask
from flask import request, jsonify
from DB import DB

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/duolingo-words/all', methods=['GET'])
def api_all():
    db = DB()
    duolingo_words = db.getAllDuolingoWords()

    return jsonify(duolingo_words)


@app.route('/api/v1/resources/duolingo-words', methods=['GET'])
def api_filter():
    print('entro 1')
    db = DB()
    query_parameters = request.args

    ipa = query_parameters.get('ipa')
    print(ipa)

    if ipa:
        ipa_duolingo_words = db.getWordsWithIpa(ipa)
    if not (ipa):
        return page_not_found(404)
    print(ipa_duolingo_words)
    return jsonify(ipa_duolingo_words)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()