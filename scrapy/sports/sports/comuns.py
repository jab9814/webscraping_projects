from datetime import datetime


def clean_list_data(data: list[str] | str) -> str:
    if isinstance(data, list):
        return "".join(data).strip()
    return data


def change_date_format(date: str, origin_format: str, target_format='%Y-%m-%d') -> str:
    if date.strip() == "":
        return ""
    try:
        day, day_number, month, year = date.split(' ')
        date = datetime.strptime(
            "/".join([day_number, month, year]), origin_format
        ).strftime(target_format)
        return date
    except Exception as e:
        print('Error en la funcion "change_date_format". Error:', e)
        return ""
