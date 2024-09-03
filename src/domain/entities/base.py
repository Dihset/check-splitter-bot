class NotLoaded:
    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "<NotLoaded>"
