from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def collaborative_recommendation(user_data, user_id):
    """Collaborative filtering based on user interaction similarity."""
    user_matrix = user_data.pivot(index='user_id', columns='post_id', values='rating').fillna(0)
    similarity_matrix = cosine_similarity(user_matrix)

    user_idx = np.where(user_matrix.index == user_id)[0][0]
    similar_users = similarity_matrix[user_idx].argsort()[-10:][::-1]

    recommendations = []
    for similar_user in similar_users:
        recommendations.extend(user_matrix.iloc[similar_user].nlargest(10).index)

    return recommendations[:10]
