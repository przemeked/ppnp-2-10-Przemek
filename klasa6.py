class MyException(Exception):
    def __init__(selfs, message):
        super().__init__(message)

try:
    raise MyException("Wystąpił wyjątek")
except MyException:
    print("Wystapił wyjątek mMyException")

except Exception as e:
    print("Błąd", e)