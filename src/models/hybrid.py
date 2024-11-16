def hybrid_recommendation(content_recommendations, collaborative_recommendations):
    """Combine recommendations from content-based and collaborative approaches."""
    hybrid = list(set(content_recommendations + collaborative_recommendations))
    return hybrid[:10]
