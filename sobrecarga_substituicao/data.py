from datetime import date
class Data:
    def __init__(self, data):
        if isinstance(data, str):
            self._data = date.fromisoformat(data)
        if isinstance(data, date):
            self._data = date

    def __str__(self):
        return f'{self._data.day}/{self._data.month}/{self._data.year}'