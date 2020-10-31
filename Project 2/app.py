import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

postgres = 'postgres'
password = 'postgres'

#################################################
# Database Setup
#################################################
engine = create_engine(
    f"postgres://{postgres}:{password}@localhost:5432/Project_2")
conn = engine.connect()



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/indeed<br/>"
    )


@app.route("/indeed")
def indeed():
    # # Create our session (link) from Python to the DB
    # session = Session(engine)

    # Query all data
    results = pd.read_sql("SELECT * FROM indeed", conn)

    P2 = results.to_dict(orient='records')
    # session.close()

    # # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)
    return jsonify(P2)


if __name__ == '__main__':
    app.run(debug=True)
