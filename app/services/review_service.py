import asyncio
from app.models.review_request import (
    TranslationReviewRequest,
    TranslationReviewBatchRequest,
)
from app.models.review_response import (
    TranslationReviewResponse,
    TranslationReviewBatchResponse,
)
from app.services.translation_quatity_model import (
    TranslationQualityModel,
)


class ReviewService:

    def __init__(self):
        self.model = TranslationQualityModel()

    async def review(
        self,
        request: TranslationReviewRequest,
    ) -> TranslationReviewResponse:

        # Giả định self.model.evaluate trả về điểm thô từ 0.0 đến 1.0 (ví dụ: 0.82)
        raw_score = self.model.evaluate(
            source_text=request.source_text,
            translated_text=request.translated_text,
            source_language=request.source_language,
            target_language=request.target_language,
            context=request.context,
        )

        # Đổi sang hệ điểm số 100 (ví dụ: 0.82 -> 82.0)
        score = round(raw_score * 100, 2)

        # CẬP NHẬT THANG ĐO PHÙ HỢP VỚI COMET:
        # - Trên 82: Bản dịch xuất sắc, chuẩn con người dịch (Hiếm khi COMET cho > 90)
        # - Từ 75 đến 82: Bản dịch tốt, lưu loát, đúng nghĩa
        # - Từ 65 đến 75: Tạm ổn nhưng cần kiểm tra lại lỗi nhỏ
        # - Dưới 65: Bản dịch tệ hoặc sai lệch nghĩa hoàn toàn
        if score >= 82:
            quality = "excellent"
        elif score >= 75:
            quality = "good"
        elif score >= 65:
            quality = "needs_review"
        else:
            quality = "poor"

        return TranslationReviewResponse(
            translation_id=request.translation_id,
            score=score,
            quality=quality,
            issues=[],
            suggestion=None,
        )

    async def review_batch(
        self,
        request: TranslationReviewBatchRequest,
    ) -> TranslationReviewBatchResponse:

        tasks = [self.review(item) for item in request.items]
        results = await asyncio.gather(*tasks)

        return TranslationReviewBatchResponse(
            items=list(results)
        )
