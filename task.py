from logger_config import task_logger

class Task:
    def __init__(self, id, periodo, deadline, tiempo_ejecucion, tiempo_inicio):
        self.id = id
        self.periodo = periodo
        self.deadline = deadline
        self.tiempo_ejecucion = tiempo_ejecucion
        self.tiempo_inicio = tiempo_inicio
        self.tiempo_final = None		
        task_logger.info(f"Task created: {self.id}")