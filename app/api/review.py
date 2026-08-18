from fastapi import APIRouter

from app.models.review_request import (
    TranslationReviewRequest,
    TranslationReviewBatchRequest,
)

from app.models.review_response import (
    TranslationReviewResponse,
    TranslationReviewBatchResponse,
)

from app.services.review_service import ReviewService


router = APIRouter(
    prefix="/api/review",
    tags=["Translation Review"],
)

review_service = ReviewService()


@router.post(
    "/evaluate",
    response_model=TranslationReviewResponse,
)
async def evaluate_translation(
    request: TranslationReviewRequest,
):
    return await review_service.review(request)


@router.post(
    "/evaluate-batch",
    response_model=TranslationReviewBatchResponse,
)
async def evaluate_batch(
    request: TranslationReviewBatchRequest,
):
    return await review_service.review_batch(request)