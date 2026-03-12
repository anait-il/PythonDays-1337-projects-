from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": self.stream_id,
            "type": self.stream_type
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental"
        self.stream_name = "Sensor"

        print(f"Initializing {self.stream_name} Stream...")
        print(
            f"Stream ID: {self.get_stats()['id']},", end=" ")
        print(f"type: {self.get_stats()['type']} Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        if isinstance(data_batch, list):
            reading = len(data_batch)
            temp = ([float(temp)
                     for t in data_batch
                     for tp, temp in (t.split(":"),)
                     if tp == "temp"])
            len_temp = len(temp)
            total = sum(temp) / len_temp if temp else 0
            return f"{reading} reading processed, avg temp: {total}°C"
        else:
            raise ValueError("Sensor_batch not a list, enter a valid stream")


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial"
        self.stream_name = "Transaction"

        print(f"Initializing {self.stream_name} Stream...")
        print(f"Stream ID: {self.get_stats()['id']},", end=" ")
        print(f"type: {self.get_stats()['type']} Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        if isinstance(data_batch, list):
            operations = len(data_batch)
            net_flow = sum([int(amount)
                            if act == "buy" else -int(amount)
                            for t in data_batch
                            for act, amount in [t.split(":")]])
            return f"{operations} operations, +{net_flow} units"
        else:
            raise ValueError("data_batch not list, enter a valid stream")


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System"
        self.stream_name = "Event"

        print(f"Initializing {self.stream_name} Stream...")
        print(f"Stream ID: {self.get_stats()['id']},", end=" ")
        print(f"type: {self.get_stats()['type']} Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        if isinstance(data_batch, list):
            events = len(data_batch)
            errors = len([1 for i in data_batch if i == "error"])
            return f"{events} events, {errors} error detected"
        else:
            raise ValueError("event_batch not a list, enter a valid stream")


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[str]]) -> None:

        for stream in self.streams:
            batch = batches.get(stream.stream_name, [])
            process = stream.process_batch(batch).split(", ", 1)
            if isinstance(stream, (TransactionStream, EventStream)):
                print(
                    f"- {stream.stream_name} data: {process[0]} processed")
            else:
                print(
                    f"- {stream.stream_name} data: {process[0]}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    try:
        sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
        sensor = SensorStream("SENSOR_001")
        batch_form = ", ".join(sensor_batch)
        print(f"Processing sensor batch: [{batch_form}]")
        print(f"Sensor analysis: {sensor.process_batch(sensor_batch)}")
    except Exception as e:
        print(f"Error, {e}")

    print()
    try:
        trans_batch = ["buy:100", "sell:150", "buy:75"]
        transaction = TransactionStream("TRANS_001")
        batch_form = ", ".join(trans_batch)
        print(f"Processing transaction batch: [{batch_form}]")
        print(
            f"Transaction analysis: {transaction.process_batch(trans_batch)}")
    except Exception as e:
        print(f"Error: {e}")

    print()
    try:
        event_batch = ["login", "error", "logout"]
        event = EventStream("EVENT_001")
        batch_form = ", ".join(event_batch)
        print(f"Processing event batch: [{batch_form}]")
        print(f"Event analysis: {event.process_batch(event_batch)}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Polymorphic Stream Processing ===")
    mixed_batch = {
        "Sensor": ["temp:22.5", "temp:11.0"],
        "Transaction": ["buy:100", "sell:150", "buy:75", "sell:10"],
        "Event": ["login", "error", "logout"]
    }
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    print("Processing mixed stream types through unified interface...\n")
    batches = [mixed_batch]
    i = 1
    for batch in batches:
        print(f"Batch {i} Results:")
        processor.process_all(batch)
        i += 1

    print("\nStream filtering active: High-priority data only")
    sensor_filter = sensor.filter_data(mixed_batch["Sensor"], "temp")
    tr_batch = mixed_batch["Transaction"]
    transaction_filter = transaction.filter_data(tr_batch, "sell")

    print(f"Filtered result: {len(sensor_filter)} critical sensor ", end="")
    print(f"alerts, {len(transaction_filter)} large transaction")

    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}")
