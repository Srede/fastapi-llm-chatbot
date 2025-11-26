from fastapi import APIRouter
from .schemas import ChatRequest, ChatResponse, SimilarQuestion
from .loader import load_questions
from .vectorstore import build_vector_store, search_similar
from .llm import validate_question, refine_question, generate_answer

router = APIRouter(prefix="/chat")

questions = load_questions()
index, questions_full = build_vector_store(questions)


@router.post("/", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    user_msg = req.message

    # 1) validate
    is_valid = validate_question(user_msg)
    if not is_valid:
        return ChatResponse(
            original_question=user_msg,
            is_valid=False,
            refined_question=None,
            similar_questions=[],
        )

    # 2) refine
    refined = refine_question(user_msg)

    # 3) semantic search over question.json
    related_dicts = search_similar(refined, index, questions_full)

    # convert dicts -> SimilarQuestion models
    related_models = [SimilarQuestion(**q) for q in related_dicts]

    # 4) final answer using context
    answer = generate_answer(refined, related_dicts)

    # For GitHub / interviewer you can either:
    # - return only the refinement + similar list, OR
    # - also include answer in a separate field / in refined_question text.
    # Here we keep your schema and put LLM answer into refined_question text.
    return ChatResponse(
        original_question=user_msg,
        is_valid=True,
        refined_question=answer,
        similar_questions=related_models,
    )
