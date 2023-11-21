import time

from src.generate_fake_data.main import FakeGenerate


def main() -> None:
    fake = FakeGenerate()
    aux = 5
    while aux !=0:
        print(fake.generate_data_fake())
        time.sleep(3)
        aux -=1

if __name__ == "__main__":
    main()