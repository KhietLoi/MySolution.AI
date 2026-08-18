from abc import ABC, abstractmethod


class ModelService(ABC):

    @abstractmethod
    async def evaluate(
        self,
        source_text: str,
        translated_text: str,
        source_language: str,
        target_language: str,
        context: str | None = None,
    ) -> float:
        pass

    @abstractmethod
    async def evaluate_batch(
        self,
        items: list[dict],
    ) -> list[float]:
        pass