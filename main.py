from src.api.preprocess import preprocess_data
from src.models.content_based import content_based_recommendation
from src.models.collaborative import collaborative_recommendation
from src.models.hybrid import hybrid_recommendation

if __name__ == "__main__":
    data = preprocess_data()

    # Example: Content-based recommendation
    content_recs = content_based_recommendation(data, user_viewed_ids=[1, 2, 3])
    print("Content-Based Recommendations:", content_recs)

    # Example: Collaborative filtering recommendation
    collab_recs = collaborative_recommendation(data, user_id=1)
    print("Collaborative Recommendations:", collab_recs)

    # Hybrid model
    hybrid_recs = hybrid_recommendation(content_recs, collab_recs)
    print("Hybrid Recommendations:", hybrid_recs)
