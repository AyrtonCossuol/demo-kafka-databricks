import time
from confluent_kafka import Producer
import socket

from src.generate_fake_data.main import FakeGenerate


def main() -> None:
    fake = FakeGenerate()
    # aux = 5
    # while aux !=0:
    #     print(fake.generate_data_fake())
    #     time.sleep(3)
    #     aux -=1



    conf = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': socket.gethostname()
    }

    producer = Producer(conf)
    topic = 'demo-test-1'

    producer.produce(topic, key="key", value=fake.generate_data_fake())
    producer.flush()

if __name__ == "__main__":
    main()