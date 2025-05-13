import requests
from connection import SessionLocal
from models import Gestor, getCobranca
import logging
from logging.handlers import RotatingFileHandler
from database.db_controller import getCommit
from database.logger import payload_logger 

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
        "commit": getCommit       # Criar separator -> commit das alterações no banco e armazenar na api, ou deixar como opção de visualização por email como envio de um arquivo 
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
    except requests.exceptions.RequestException as e:
         payload_logger.error(f"Erro de envio de dados {e}")