from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def calc_similarity_scores(strings):
    """Returns a normalized vector of similarity scores corresponding to the strings.

    :param list strings: The collection of strings for which the function
    computes similarity scores.
    """
    # Find Tfidf pairwise scores
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(strings)
    pairwise_scores = (tfidf * tfidf.T).A
    # Convert pairwise scores into 1 score for each string
    scores = []
    for vec in pairwise_scores:
        result.append(np.linalg.norm(vec))
    # Normalize scores
    scores_array = np.array(result)
    return scores_array / np.linalg.norm(scores_array)

def calc_popularity(scores):
    """Returns an array popularity [1, 10] based on percentile w.r.t other scores.
    """
    quantiles = [10*i for i in range(1,10)]
    percentiles = np.percentile(scores, quantiles)
    return np.digitize(scores, percentiles) + 1
