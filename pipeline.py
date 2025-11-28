from agents.planner_agent import planner_agent
from agents.search_agent import rag_agent as search_agent
from agents.summarizer_agent import summarizer_agent
from agents.recommender_agent import recommender_agent
from agents.reflective_agent import reflective_agent


def run_pipeline(user_query, filters):
    print("\n===== RUN PIPELINE =====")

    # 1. Planner
    plan = planner_agent(user_query)
    print(f"[Pipeline] Plan: {plan}")

    # 2. RAG Search
    evidence = search_agent(user_query)

    # 3. Summarizer (Groq - FREE)
    summary = summarizer_agent(evidence)

    # 4. Recommender
    recommendations = recommender_agent(filters)

    # 5. Reflective
    score = reflective_agent(summary, recommendations, user_query)

    return summary, recommendations, score
