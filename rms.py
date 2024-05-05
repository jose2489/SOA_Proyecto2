from scheduler import Scheduler

class RMS(Scheduler):
    def ejecutar(self):
        self.tareas.sort(key=lambda x: x.periodo)
        for tarea in self.tareas:
            if tarea.tiempo_inicio <= self.tiempo_actual and tarea.tiempo_final is None:
                tarea.tiempo_final = self.tiempo_actual + tarea.tiempo_ejecucion
                self.log.append(f"Tarea {tarea.id} completada en {tarea.tiempo_final}.")
                break
        self.actualizar_tiempo()