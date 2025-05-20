from logger import send_status_db_logger , orm_errors_logger
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from database.logger import send_status_db_logger, orm_errors_logger, commit_logger

mutation_log = [] 

def get_data(session, obj):
    try:
        mutation_log.append(("GET", obj, None))
        session.get(obj)
    except SQLAlchemyError as db_err :  
        session.rollback()
        orm_errors_logger.error(f"Erro ao atualizar objeto ao banco: {db_err}")

def add_data(session, obj):
    try:
        mutation_log.append(("ADD", obj, None))
        session.add(obj)
        send_status_db_logger(f"Objeto adicionado: {obj}")
    except SQLAlchemyError as db_err :  # erro na integração com banco via ORM
        session.rollback()
        orm_errors_logger.error(f"Erro ao inserir objeto ao banco: {db_err}")

def delete_data(session, obj):
    try:
        mutation_log.append(("DELETE", obj, None))
        session.delete(obj)
        send_status_db_logger(f"Objeto excluido: {obj}")
    except SQLAlchemyError as db_err :
        session.rollback()
        orm_errors_logger.error(f"Erro ao excluir objeto no banco: {db_err}")

def commit_changes(session):
    try:
        session.commit()
        send_status_db_logger.info("Commit finalizado")
    except SQLAlchemyError as err : 
        orm_errors_logger.error(f"Erro ao realizar commit: {err}")
        session.rollback()

def trackMutationOperation(old, new):
    diffs = {}
    if old and new:
        for attr in new.__dict__:
            if not attr.startswitch('_') and getattr(old, attr, None) != getattr(new, attr, None):
                diffs[attr] = {
                        'old': getattr(old, attr, None),
                        'new': getattr(new, attr, None)
                    }
    elif old and new :
            diffs = {"status": "deletado", "conteúdo": old.__dict__}
    elif new and old :
            diffs = {"status": "adicionado", "conteúdo": new.__dict__}

    if diffs:
        diffs['timestamp'] = datetime.now().isoformat()
        send_status_db_logger.info(f"Fatura com alteração: {diffs}")
    return diffs

def getCommit():
    commits = []

    for action, old, new in mutation_log :
        diff = trackMutationOperation(old, new)
        commit_entry = {
            "action": action,
            "diff": diff
        }

        commit_logger.info(f"Commit registrado: {commit_entry}")
        commits.append(commit_entry)

    return commits()