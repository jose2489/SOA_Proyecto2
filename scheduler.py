class Scheduler:
    def __init__(self, mode='RMS'):
        self.tareas = []
        self.tiempo_actual = 0
        self.log = []
        self.mode = mode  # This will hold the scheduling mode (RMS or EDF)

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def ejecutar(self):
        # Continue until all tasks are completed or cannot be executed
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

    def actualizar_tiempo(self):
        self.tiempo_actual += 1
