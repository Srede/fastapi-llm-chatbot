from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


# Uses OPENAI_API_KEY from environment
llm = ChatOpenAI(
    model="gpt-4.1-mini",   # if this ever errors, switch to "gpt-4o-mini"
    temperature=0.2,
)


def validate_question(user_question: str) -> bool:
    """
    Return True if this looks like a well-posed math question, else False.
    """
    prompt = f"""
You are a strict validator. The user provides a sentence.

Determine if it is a well-posed mathematical QUESTION
(e.g., algebra, calculus, linear algebra, topology, PDEs, analysis,
probability, statistics, etc.).

Answer ONLY "YES" or "NO".

User input:
{user_question}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    text = response.content.strip().upper()
    return text.startswith("Y")


def refine_question(user_question: str) -> str:
    """
    Rewrite the user's math question with better grammar and clarity,
    without changing its meaning.
    """
    prompt = f"""
You are a mathematical editor.

Rewrite the following mathematical question to improve grammar and clarity.
Do NOT change its meaning. Return ONLY the revised question.

Original question:
{user_question}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()


def generate_answer(user_message: str, related_questions: str) -> str:
    """
    Use the similar questions as context and answer the user's math question.
    """
    prompt = f"""
You are a helpful math tutor.

CONTEXT (similar questions from our database):
{related_questions}

USER QUESTION:
{user_message}

Use the context if it helps. If the question is unrelated to math,
say politely that this service is only for mathematics questions.
Provide a clear, step-by-step answer when possible.
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()








#from langchain.chat_models import ChatOpenAI
#from langchain.schema import HumanMessage # type: ignore
#import os
#llm = ChatOpenAI(model="gpt-5", temperature=0)
#def generate_answer(user_message, related_questions):
    #prompt = f"""# USE the context to answer.
    #CONTEXT:
    #{related_questions}
    #USER QUESTION:
    #{user_message}
    #"""
    #return llm([HumanMessage(content=prompt)]).content