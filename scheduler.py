from logger_config import scheduler_logger

class Scheduler:
    def __init__(self, mode='RMS'):
        self.tareas = []
        self.tiempo_actual = 0
        self.log = []
        self.mode = mode  # This will hold the scheduling mode (RMS or EDF)
        scheduler_logger.info(f"Scheduler initialized in {mode} mode")
        self.stats = {'executed': 0, 'missed_deadlines': 0, 'idle_periods': 0}

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        scheduler_logger.info(f"Task {tarea.id} added to scheduler")

    def ejecutar(self):
        # Continue until all tasks are completed or cannot be executed
        scheduler_logger.info("Scheduler execution started")
        while True:
            # Sort tasks based on the mode
            if self.mode == 'RMS':
                self.tareas.sort(key=lambda x: x.periodo)
            elif self.mode == 'EDF':
                self.tareas.sort(key=lambda x: x.deadline)

            executed_any = False  # To track if any task was executed in the current cycle
            for tarea in self.tareas:
                # Check if task is ready and not yet completed
                if tarea.tiempo_inicio <= self.tiempo_actual and tarea.tiempo_final is None:
                    tarea.tiempo_final = self.tiempo_actual + tarea.tiempo_ejecucion
                    self.log.append(f"Tarea {tarea.id} completada en {tarea.tiempo_final}.")
                    executed_any = True  # Task was executed
                    break  # Execute one task per cycle

            if not executed_any:
                if any(t.tiempo_final is None for t in self.tareas):
                    self.tiempo_actual += 1  # No task executed, move time forward
                else:
                    break  # All tasks completed
                    # Calculate statistics at the end
        scheduler_logger.info("Scheduler execution finished")
        for task in self.tareas:
            if task.tiempo_final > task.deadline:
                self.stats['missed_deadlines'] += 1

    def actualizar_tiempo(self):
        self.tiempo_actual += 1
