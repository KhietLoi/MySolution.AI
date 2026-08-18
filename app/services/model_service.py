from abc import ABC, abstractmethod


class ModelService(ABC):

    @abstractmethod
    def evaluate(
        self,
        source_text: str,
        translated_text: str,
        source_language: str,
        target_language: str,
        context: str | None = None,
    ) -> float:
        pass

    @abstractmethod
    def evaluate_batch(
        self,
        items: list[dict],
    ) -> list[float]:
        pass