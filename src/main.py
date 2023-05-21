from src.modules.get import get
from src.modules.store import store


if __name__ == '__main__':
    store("34-78", 'RED')
    store("31-41", 'YELLOW')
    store("64-98", 'GREEN')

    print(get("31"))
    print(get("39"))
    print(get("50"))
    print(get("68"))
    print(get("91"))
    print(get("99"))

    store("90-99", 'BLUE')

    print(get("91"))
    print(get("99"))
