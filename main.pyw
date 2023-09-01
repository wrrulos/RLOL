from src.startup import Startup

from src.utilities.exception_handler import ExceptionHandler


if __name__ == "__main__":
    exception_handler = ExceptionHandler('error_log.txt')
    
    try:
        Startup.run()

    except (Exception, KeyboardInterrupt) as e:
        exception_handler.log_exception(type(e), str(e))