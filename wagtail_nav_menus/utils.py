from typing import Protocol


class DateTimeLike(Protocol):
    def isoformat(self) -> str: ...


def date_handler(obj: DateTimeLike) -> str:
    if hasattr(obj, "isoformat"):
        return obj.isoformat()
    else:
        raise TypeError(f"Unserializable object {obj} of type {type(obj)}")
