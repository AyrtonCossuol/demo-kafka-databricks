import time
from confluent_kafka import Producer
import socket

from src.generate_fake_data.main import FakeGenerate


def main() -> None:
    fake = FakeGenerate()

    conf = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': socket.gethostname()
    }

    producer = Producer(conf)
    topic = 'demo-fake-data'

    qt_exec_test = 0
    while True:
        producer.produce(topic, key="key", value=fake.generate_data_fake())
        producer.flush()
        qt_exec_test += 1
        print(f"Message {qt_exec_test} Sent")
        time.sleep(3)

if __name__ == "__main__":
    main()