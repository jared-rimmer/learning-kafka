from dataclasses import dataclass
from dataclasses_avroschema import AvroModel
from kafka import KafkaConsumer, KafkaProducer

import random


@dataclass
class UserModel(AvroModel):
    "A User"
    name: str
    age: int

    class Meta:
        namespace = "User.v1"
        aliases = ["user-v1"]


def send(total_events=10):

    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        key_serializer=str.encode,
        compression_type="gzip",
    )

    for event_number in range(1, total_events + 1):

        print(f"Sending event number: {event_number}")

        user = UserModel(
            name=random.choice(["Eve", "Jared", "David", "Holly"]),
            age=random.randint(1, 50),
        )

        message = user.serialize()

        producer.send("test_topic", key=user.name, value=message)
        producer.send("another_topic", key=user.name, value=message)

    print("Stopping the producer")


def consume():

    consumer = KafkaConsumer(
        "test_topic",
        "another_topic",
        bootstrap_servers="localhost:9092",
        client_id="my-first-consumer",
        group_id="test-group",
        consumer_timeout_ms=10000,
    )

    for msg in consumer:

        print(f"Message Received: {msg.value} at {msg.timestamp}")

        user = UserModel.deserialize(msg.value)

        print(f"Message deserialised: {user}")

    print("Stopping the consumer")


if __name__ == "__main__":
    send()
    consume()
