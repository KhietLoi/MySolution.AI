from app.services.translation_quality_model import (
    TranslationQualityModel
)


class ModelManager:

    def __init__(self):
        self.model = TranslationQualityModel()

    def load(self):
        self.model.load()

    def get_model(self):
        return self.model