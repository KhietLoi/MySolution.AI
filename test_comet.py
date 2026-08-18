from app.services.translation_quatity_model import (
    TranslationQualityModel,
)


model = TranslationQualityModel()

score = model.evaluate(
    source_text="Login",
    translated_text="Đăng kí",
    source_language="en",
    target_language="vi",
)

print("COMET SCORE:", score)
print("SCORE 0-100:", round(score * 100, 2))