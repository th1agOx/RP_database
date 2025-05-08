import requests
from connection import SessionLocal
from models import Gestor
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

handlers = RotatingFileHandler("requests.py", maxBytes=1000000, backupCount=5)

session = SessionLocal()

gestor = session.query(Gestor).all()

data = []

for gestor_table in gestor :

    document_detail = [
        {
            "telefone": c.telefone,
            "total": c.valor_mensal
        }

        for c in gestor.cobranca
    ]

    payload = {
        "email_gestor": gestor_table.email_gestor,
        "titulo": "Detalhes de Cobrança",
        "centro_de_custo": gestor_table.numero_cc,
        "details": document_detail
    }

    data.append(payload)

session.close

# atualizar verificações de envio do payload e fazer o envio com requests.post
url = "10.171.155.50:5000/api/send-email-carga"

for payload in data :
    try:
        response = requests.post(url, json=payload)
        logging.info(f"Enviado para {payload[gestor_table.email_gestor]}, status:{response.status_code}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro de envio de dados {e}")