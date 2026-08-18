from comet import download_model, load_from_checkpoint

from app.services.model_service import ModelService


class TranslationQualityModel(ModelService):

    MODEL_NAME = "Unbabel/wmt20-comet-qe-da"

    def __init__(self):
        self.model = None

    def load(self):
        if self.model is not None:
            return

        print("Loading COMET model...")

        model_path = download_model(
            self.MODEL_NAME
        )

        self.model = load_from_checkpoint(
            model_path
        )

        print("COMET model loaded.")

    def evaluate(
        self,
        source_text: str,
        translated_text: str,
        source_language: str,
        target_language: str,
        context: str | None = None,
    ) -> float:

        if self.model is None:
            self.load()

        data = [
            {
                "src": source_text,
                "mt": translated_text,
            }
        ]

        output = self.model.predict(
            data,
            batch_size=1,
            gpus=0,
        )

        return float(output.scores[0])

    def evaluate_batch(
        self,
        items: list[dict],
    ) -> list[float]:

        if self.model is None:
            self.load()

        data = [
            {
                "src": item["source_text"],
                "mt": item["translated_text"],
            }
            for item in items
        ]

        output = self.model.predict(
            data,
            batch_size=4,
            gpus=0,
        )

        return [
            float(score)
            for score in output.scores
        ]