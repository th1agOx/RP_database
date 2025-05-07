import os  
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),' ')))

from database.connection import get_session
from database.models import Base

from flask import Flask, jsonify  

app = Flask(__name__)

@app.route("/gestores", methods=["GET"])
def listener_gestores():
    session = get_session()
    gestores = session.query(Base).all()
    data = [
        {
            "id" : g.id,
            "nome" : g.nome,
            "email" : g.email_gestor
        }
        for g in gestores
    ]
    session.close()
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)