import logging
from logging.handlers import RotatingFileHandler
import requests
from connection import SessionLocal 
from logger import payload_logger 
from models import Gestor, getCobranca
from db_controller import getCommit, Request

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
handlers = RotatingFileHandler("requests.py", maxBytes=1000000, backupCount=5)

session = SessionLocal()

gestores = session.query(Gestor).all()

data = []

for gestor in gestores :
    payload = {
        "email_gestor": gestor.email_gestor,
        "titulo": "Detalhes de Cobrança",  
        "centro_de_custo": gestor.numero_cc,
        "total_cc": gestor.valor_mensal_total,
        "details": getCobranca,
        "commit": getCommit       
    }

    data.append(payload)

session.close

url = "10.171.155.50:5000/api/send-email-carga"

for payload in data :
    try:
        response = requests.post(url, json=payload)
        payload_logger.info(
            f"Enviado para API ({payload['email_gestor']}), status: {response.status_code}"
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as req_err:
        payload_logger.error(f"Erro de envio de dados {req_err}")