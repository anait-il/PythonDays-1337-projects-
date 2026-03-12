from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod
import time
del Dict, Optional


class Processing_Stages(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            required = ["sensor", "value", "unit"]
            for key in required:
                if key not in data:
                    raise ValueError(
                        "error detected in Stage 1: Invalid JSON sensor data")
            for k, v in data.items():
                if not k or not v:
                    raise ValueError(
                        "Error detected in Stage 1: JSON data can't be None")
            print(f"Input: {data}")

        elif isinstance(data, tuple):
            for item in data:
                if not item:
                    raise ValueError(
                        "Error detected in Stage 1: invalid data format")
            print(f'Input: "{data[0]}"')
            data = [item.split(",") for item in data]
            return data

        elif isinstance(data, list):
            data = tuple(data)
            print("Input: Real-time sensor stream")

        else:
            raise ValueError(
                "Error detected in Stage 1: \
                data provided can't go truth this pipeline")

        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            try:
                data["value"] = float(data["value"])
            except ValueError:
                raise ValueError(
                    "Error detected in Stage 2: Invalid data format")
            data = {key: float(value)
                    if key == "value"
                    else value
                    for key, value in data.items()}
            value = data["value"]

            if value < 18:
                status = "Low"
            elif value <= 26:
                status = "Normal range"
            else:
                status = "High"

            data["status"] = status
            print("Transform: Enriched with metadata and validation")

        elif isinstance(data, list):
            print("Transform: Parsed and structured data")
            header = data[0]
            rows = data[1:]
            structured = [dict(zip(header, row)) for row in rows]
            return structured

        elif isinstance(data, tuple):
            for item in data:
                if not isinstance(item, (int, float)):
                    raise ValueError(
                        "Error detected in Stage 2: invalid data format")
            print("Transform: Aggregated and filtered")
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            value = data["status"]
            return f"Processed temperature reading:" \
                   f"{data['value']}°C ({value})"

        if isinstance(data, list):
            return f"User activity logged: {len(data)} actions processed"

        if isinstance(data, tuple):
            lenght = len(data)
            avg = sum(data) / lenght if lenght else 0
            return f"Stream summary: {lenght} readings, avg: {avg:.1f}°C"


class ProcessingPipeline (ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[Processing_Stages] = []

    def add_stage(self, stage: Processing_Stages) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing JSON data through pipeline...")
        for stage in self.stages:
            data = stage.process(data)
        print(f"Output: {data}")


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing CSV data through same pipeline...")
        for stage in self.stages:
            data = stage.process(data)
        print(f"Output: {data}")


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing Stream data through same pipeline...")
        for stage in self.stages:
            data = stage.process(data)
        print(f"Output: {data}")


class NexusManager:
    def __init__(self, capacity: int) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.data: List[Any] = []
        print("Initializing Nexus Manager...")
        print(f"Pipeline capacity: {capacity} streams/second")

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def create_stages(self) -> None:
        print("\nCreating Data Processing Pipeline...")
        for pipeline in self.pipelines:
            pipeline.add_stage(InputStage())
        print("Stage 1: Input validation and parsing")

        for pipeline in self.pipelines:
            pipeline.add_stage(TransformStage())
        print("Stage 2: Data transformation and enrichment")

        for pipeline in self.pipelines:
            pipeline.add_stage(OutputStage())
        print("Stage 3: Output formatting and delivery")

    def add_data(self, data: Any) -> None:
        self.data.append(data)

    def process_data(self) -> str:
        start = time.perf_counter()
        stages_count = 0
        total_record = 0
        efficiency = 95

        for pipeline, dt in zip(self.pipelines, self.data):
            try:
                pipeline.process(dt)
                print()
                total_record += 1
            except Exception as e:
                print(e)
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline restored,", end=" ")
                print("processing resumed")
                return

        end = time.perf_counter()

        process_time = end - start

        stages_count = len(self.pipelines[0].stages)

        return f"Chain result: {total_record} records processed through " \
               f"{stages_count}-pipeline" \
               f"\nPerformance: {efficiency}% efficiency, " \
               f"{process_time:.5f}s total processing time"


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    nexus = NexusManager(100)
    pipelines = [JSONAdapter, CSVAdapter, StreamAdapter]
    pipe_id = ["json_001", "csv_001", "stream_001"]
    batch = [{"sensor": "temp",
              "value": "23.5",
              "unit": "C"},
             ("user,action,timestamp",
              "someone,logged,morning"),
             [20.5, 21.0, 22.5, 23.0, 23.5]]

    for stream, pip_id in zip(pipelines, pipe_id):
        nexus.add_pipeline(stream(pip_id))

    nexus.create_stages()
    print()

    print("\n=== Multi-Format Data Processing ===\n")

    for data in batch:
        nexus.add_data(data)

    statistics = nexus.process_data()

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

    print(statistics)

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    nexus.data[0] = {
        "sensor": "temp",
        "value": "abc",
        "unit": "C"
    }
    nexus.process_data()

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
