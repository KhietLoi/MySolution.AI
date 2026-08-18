from app.models.review_request import (
    TranslationReviewRequest,
    TranslationReviewBatchRequest,
)

from app.models.review_response import (
    TranslationReviewResponse,
    TranslationReviewBatchResponse,
)


class ReviewService:

    async def review(
        self,
        request: TranslationReviewRequest,
    ) -> TranslationReviewResponse:

        return TranslationReviewResponse(
            translation_id=request.translation_id,
            score=95.0,
            quality="excellent",
            issues=[],
            suggestion=None,
        )

    async def review_batch(
        self,
        request: TranslationReviewBatchRequest,
    ) -> TranslationReviewBatchResponse:

        results = []

        for item in request.items:
            result = await self.review(item)
            results.append(result)

        return TranslationReviewBatchResponse(
            items=results
        )