from models.temp_model import push_temperature_factory
import time
from rx import create


def main():
    source = create(push_temperature_factory)

    source.subscribe(
        on_next=lambda event: print(event),
        on_error=lambda e: print("Error Occurred: {0}".format(e)),
        on_completed=lambda: print("Done!"),
    )


if __name__ == "__main__":
    main()
