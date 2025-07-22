import functools
from typing import Callable, Optional, Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования выполнения функции.

    Логирует:
        - Успешное выполнение функции с сообщением "<имя_функции> ok"
        - Ошибки с сообщением "<имя_функции> error: <тип_ошибки>. Inputs: <args>, <kwargs>"

    Аргументы:
        filename (str, optional): Путь к файлу для логирования.
            Если не указан, логирование производится в консоль.

    Возвращает:
        function: Обёрнутая функция с логированием.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обёртка функции для логирования начала, завершения и ошибок выполнения.

            Аргументы:
                *args: Позиционные аргументы целевой функции.
                **kwargs: Именованные аргументы целевой функции.

            Возвращает:
                Результат выполнения целевой функции.

            Исключения:
                Пробрасывает любые исключения, возникшие в целевой функции.
            """
            log_output: str = ""
            try:
                result = func(*args, **kwargs)
                log_output = f"{func.__name__} ok"
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_output = (f"{func.__name__} error: {error_type}. "
                              f"Inputs: {args}, {kwargs}")
                raise
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_output + "\n")
                else:
                    print(log_output)
        return wrapper  # type: ignore
    return decorator
