from flask import Flask, Response

from pymongo import Connection
from pymongo.errors import ConnectionFailure
from bson.json_util import dumps

app = Flask(__name__)
app.debug = True


try:
    conn = Connection(host="localhost", port=27017)
except ConnectionFailure, e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)
db = conn['50Shades']

@app.route("/")
def hello():
    return "50 Shades of Hello World!"


@app.route("/year")
def yearly():
    """
        In this function we use the Aggregation framework to convert the data
        to the structure that our D3 needs.

        We could have done this in a different way, or even when inserting the data.

        Its a good example of how important is to know your tools.

    """
    pipeline = [{ '$project' : { '_id' : 0 ,'x' : "$_id.year" , 'y' : {'$ifNull': ['$value.relative', 0] }}}]
    ma_col = db.command('aggregate', 'ma_count_by_year', pipeline=pipeline)
    re_col = db.command('aggregate', 're_count_by_year', pipeline=pipeline)
    marqueze = {'key': 'Marqueze', 'values': ma_col['result']}
    reroticos = {'key': 'Relatos Eroticos', 'values': re_col['result']}

    result = [marqueze, reroticos]

    return Response(
        response=dumps(result),
        status=200,
        headers=None,
        mimetype='application/json',
        content_type=None,
        direct_passthrough=False
    )

@app.route("/month")
def monthly():
    pipeline = [{ '$project' : { '_id' : 0 ,'x' : "$_id.month" , 'y' : {'$ifNull': ['$value.relative', 0] }}}]
    ma_col = db.command('aggregate', 'ma_count_by_month', pipeline=pipeline)
    re_col = db.command('aggregate', 're_count_by_month', pipeline=pipeline)
    marqueze = {'key': 'Marqueze', 'values': ma_col['result']}
    reroticos = {'key': 'Relatos Eroticos', 'values': re_col['result']}

    result = [marqueze, reroticos]

    return Response(
        response=dumps(result),
        status=200,
        headers=None,
        mimetype='application/json',
        content_type=None,
        direct_passthrough=False
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
