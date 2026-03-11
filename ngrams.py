def generate_ngrams(word, n):
    word = "#" + word + "#"
    return set(word[i:i+n] for i in range(len(word) - n + 1))


def correct_spelling(word, dictionary, n=2):
    scores = []

    for d in dictionary:
        g1 = generate_ngrams(word, n)
        g2 = generate_ngrams(d, n)
        score = len(g1 & g2) / len(g1 | g2)
        scores.append((score, d))

    best_score, best_word = max(scores, key=lambda x: x[0])
    return best_word, best_score


dictionary = [
    "computer", "science", "engineering", "information",
    "technology", "spelling", "correction", "program"
]

misspelled = "technology"
result, score = correct_spelling(misspelled, dictionary)

print("misspelled word:", misspelled)
print("corrected word:", result)
print("Similarity score:", round(score, 2))
