from datetime import datetime

def validate_string(value: str, field_name: str, allow_digits: bool = True) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field_name} debe ser una cadena de texto.")
    if not value.strip():
        raise ValueError(f"{field_name} no puede estar vacío.")
    if not allow_digits and any(char.isdigit() for char in value):
        raise ValueError(f"{field_name} no debe contener dígitos numéricos.")
    return value.strip()

def validate_date(value: str, field_name: str, date_format: str = '%d/%m/%Y') -> str:
    try:
        datetime.strptime(value, date_format)
    except Exception:
        raise ValueError(f"{field_name} debe tener el formato {date_format}.")
    return value

def validate_integer(value, field_name: str, max_digits: int = None) -> int:
    try:
        num = int(value)
    except Exception:
        raise ValueError(f"{field_name} debe ser un número entero.")
    
    if max_digits is not None:
        if len(str(abs(num))) != max_digits:
            raise ValueError(f"{field_name} debe tener {max_digits} dígitos, se ingresaron {len(str(abs(num)))} dígitos.")
    return num


def validate_float(value, field_name: str) -> float:
    try:
        f_value = float(value)
        if f_value < 0:
            raise ValueError(f"{field_name} no puede ser negativo.")
        return f_value
    except Exception:
        raise ValueError(f"{field_name} debe ser un número.")
