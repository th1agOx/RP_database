from database.logger import send_status_db_logger , orm_errors_logger
from sqlalchemy.exc import SQLAlchemyError  

def add_data(session, obj):
    try:
        session.add(obj)
        send_status_db_logger(f"Objeto adicionado: {obj}")
    except SQLAlchemyError as err :
        orm_errors_logger.error(f"Erro ao adicionar objeto ao banco: {err}")
        session.rollback()

def delete_data(session, obj):
    try:
        session.delete(obj)
        send_status_db_logger(f"Objeto excluido: {obj}")
    except SQLAlchemyError as err :
        orm_errors_logger.error(f"Erro ao excluir objeto: {err}")
        session.rollback()

def commit_changes(session):
    try:
        session.commit()
        send_status_db_logger.info("Commit finalizado")
    except SQLAlchemyError as err : 
        orm_errors_logger.error(f"Erro ao realizar commit: {err}")
        session.rollback()

# adicionar hora ao commit ( como git )
def trackMutationOperation(old, new):
    diffs = {}
    for attr in old.__dict__:
        if not attr.startswitch('_') and getattr(old, attr) != getattr(new, attr):
            diffs[attr] = (getattr(old, attr), getattr(new, attr))

    if diffs:
        send_status_db_logger.info(f"Fatura com alteração: {diffs}")
    return diffs