from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def content_based_recommendation(posts, user_viewed_ids):
    """Generate recommendations based on content similarity."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(posts["tags"])

    # Find similarity between user-viewed posts and all others
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Rank by similarity scores
    recommendations = []
    for idx in user_viewed_ids:
        similar_indices = similarity_matrix[idx].argsort()[-10:][::-1]
        recommendations.extend(similar_indices)

    return recommendations[:10]
