import datetime

def function_logger(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            with open(log_file, 'a') as file:
                file.write(f"{func.__name__}\n")
                file.write(f"{start_time}\n")
                file.write(f"{args if args else kwargs}\n")
                try:
                    result = func(*args, **kwargs)
                    return_time = datetime.datetime.now()
                    elapsed_time = return_time - start_time
                    file.write(f"{result if result else '-'}\n")
                    file.write(f"{return_time}\n")
                    file.write(f"{elapsed_time}\n\n")
                    return result
                except Exception as e:
                    file.write(f"Error: {e}\n")
                    return None

        return wrapper
    return decorator
