import random
from collections import defaultdict
import time

# Define 50 sentences, each corresponding to a unique sign (first word may repeat)
SENTENCES = [
    'Young child learns fast',
    'Great job well done',
    'Strong people stay healthy',
    'Water one',
    'Water great',
    'One Water please',
    'One great and tasty noodles'
    ]

class CorpusEngine:
    def __init__(self, sentences):
        self.sentences = sentences
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.next_word_cache = {'word': None, 'timestamp': 0}
        self._build_transition_matrix()

    def _build_transition_matrix(self):
        for sentence in self.sentences:
            words = sentence.lower().split()
            for i in range(len(words)):
                current = words[i]
                next_word = words[i + 1] if i + 1 < len(words) else '<END>'
                self.transitions[current][next_word] += 1
            self.transitions['<START>'][words[0].lower()] += 1

    def predict_next_word(self, word_sequence):
        if not word_sequence:
            next_words = self.transitions['<START>']
        else:
            last_word = word_sequence[-1].lower()
            next_words = self.transitions[last_word]

        if not next_words:
            return None

        total = sum(next_words.values())
        probabilities = {word: count / total for word, count in next_words.items()}
        words, probs = zip(*probabilities.items())
        next_word = random.choices(words, weights=probs, k=1)[0]
        if next_word != '<END>':
            self.next_word_cache = {'word': next_word, 'timestamp': time.time()}
        return next_word if next_word != '<END>' else None

    def get_cached_next_word(self, timeout=10):
        if self.next_word_cache['word'] and (time.time() - self.next_word_cache['timestamp']) < timeout:
            return self.next_word_cache['word']
        return None

    def frame_sentence(self, word_sequence):
        predicted_text = ' '.join(word_sequence).lower()
        for sentence in self.sentences:
            sentence_lower = sentence.lower()
            if predicted_text == sentence_lower:
                return sentence
            if len(word_sequence) >= 2 and sentence_lower.startswith(predicted_text):
                last_word = word_sequence[-1].lower()
                next_word = self.predict_next_word(word_sequence)
                if not next_word or next_word == '<END>':
                    return sentence
        return None

    def frame_sentence_from_sequence(self, word_sequence):
        if not word_sequence:
            return None
        
        word_sequence_lower = [w.lower() for w in word_sequence]
        for sentence in self.sentences:
            sentence_words = sentence.lower().split()
            match_length = 0
            for i in range(len(sentence_words)):
                if i >= len(word_sequence_lower):
                    break
                if sentence_words[i] == word_sequence_lower[i]:
                    match_length += 1
                else:
                    break
            if match_length == len(word_sequence_lower) or (match_length > 0 and i + 1 == len(sentence_words)):
                return sentence
            if match_length == 1 and i == 0:
                matching_sentences = [s for s in self.sentences if s.lower().split()[0] == word_sequence_lower[0]]
                if len(matching_sentences) > 1:
                    return None
        return None

if __name__ == "__main__":
    # Test the corpus engine
    engine = CorpusEngine(SENTENCES)
    test_cases = [
        ['Hello'], ['Great'], ['Sunny'],
        ['Happy', 'face'], ['Bright', 'spark'],
        ['I'], ['Bright']  # Test with non-matching and repeated words
    ]
    for test_seq in test_cases:
        sentence = engine.frame_sentence_from_sequence(test_seq)
        print(f"Test sequence: {test_seq}")
        print(f"Framed sentence: {sentence}\\n")