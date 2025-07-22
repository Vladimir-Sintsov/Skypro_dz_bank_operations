import pytest
from src.decorators import log

# ===== Примеры тестируемых функций =====

@log()
def add(x: int, y: int) -> int:
    return x + y

@log()
def fail_divide(x: int, y: int) -> float:
    return x / y

@log(filename="test_log.txt")
def multiply(x: int, y: int) -> int:
    return x * y

@log(filename="test_log.txt")
def fail_subtract(x: int, y: int) -> int:
    raise ValueError("Test error")


# ======== Тесты консольного вывода ========

def test_console_success(capsys):
    """Проверяет, что успешный вызов функции логируется в консоль."""
    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "add ok" in captured.out.strip()


def test_console_exception(capsys):
    """Проверяет логирование ошибки и аргументов при исключении в консоль."""
    with pytest.raises(ZeroDivisionError):
        fail_divide(1, 0)
    captured = capsys.readouterr()
    assert "fail_divide error: ZeroDivisionError." in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


# ======== Тесты логирования в файл ========

def test_file_success_log(tmp_path):
    """Проверяет запись успешного выполнения функции в лог-файл."""
    log_file = tmp_path / "log_success.txt"

    @log(filename=str(log_file))
    def dummy_success():
        return 42

    result = dummy_success()
    assert result == 42

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "dummy_success ok" in content


def test_file_exception_log(tmp_path):
    """Проверяет запись ошибки и аргументов в лог-файл при исключении."""
    log_file = tmp_path / "log_error.txt"

    @log(filename=str(log_file))
    def dummy_fail(x):
        raise RuntimeError("failure")

    with pytest.raises(RuntimeError):
        dummy_fail(99)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "dummy_fail error: RuntimeError." in content
    assert "Inputs: (99,), {}" in content