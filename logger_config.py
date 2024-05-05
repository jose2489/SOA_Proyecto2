import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Sets up a logger with the specified name, log file, and log level."""
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Creating and configuring loggers
task_logger = setup_logger('task_logger', 'tasks.log')
scheduler_logger = setup_logger('scheduler_logger', 'scheduler.log')
command_logger = setup_logger('command_logger', 'commands.log')
