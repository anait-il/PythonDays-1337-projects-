
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod
del List, Dict, Union, Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f'Output: {result}')


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "data is not a numeric"
        if isinstance(data, list):
            lenght = len(data)
            total = sum(data)
            average = total / lenght if data else 0
        elif isinstance(data, (int, float)):
            lenght = 1
            total = data
            average = total / lenght
        return (
            f'Processed {lenght} numeric value, sum={total}, avg={average:.1f}'
            )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            if not data:
                return False
            for number in data:
                if not isinstance(number, (int, float)):
                    return False
            return True
        elif isinstance(data, (int, float)):
            return True
        else:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Data is not a text"
        char = len(data)
        words = len(data.split())
        return f"Processed text: {char} characters, {words} words"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Data is not a log"
        error = data.split(":")
        if len(error) > 2:
            return "Data is not a log"
        label = "ALERT" if error[0] == "ERROR" else "INFO"
        return f"[{label}] {error[0]} level detected:{error[1]}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if data.startswith("ERROR:"):
            return True
        elif data.startswith("INFO:"):
            return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    print("\nInitializing Numeric Processor...")
    print(f"Processing data: {numeric_data}")
    num = NumericProcessor()
    if not num.validate(numeric_data):
        print("Verified Failed: data not a numeric")
    else:
        print("Validation: Numeric data verified")
        result = num.process(numeric_data)
        print(result)
        print(num.format_output(result))

    print("\nInitializing Text Processor...")
    print(f'Processing data: "{text_data}"')
    text = TextProcessor()
    if not text.validate(text_data):
        print("Verified Failed: data not a text")
    else:
        print("Validation: Text data verified")
        result = text.process(text_data)
        print(text.format_output(result))

    print("\nInitializing Log Processor...")
    print(f'Processing data: "{log_data}"')
    log = LogProcessor()
    if not log.validate(log_data):
        print("Validation Failed: data not a log")
    else:
        print("Validation: Log entry verified")
        result = log.process(log_data)
        print(log.format_output(result))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [(NumericProcessor(), [1, 2, 3]),
                  (TextProcessor(), "hello world!"),
                  (LogProcessor(), "INFO: System ready")]
    i = 1
    for obj, data in processors:
        print(f"Result {i}: {obj.process(data)}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}")
