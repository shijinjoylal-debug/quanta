import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import time

# --- 1. Data Preparation ---

# Sample corpus (training data)
data = """The quick brown fox jumps over the lazy dog
Deep learning is subset of machine learning
Artificial intelligence is the future of technology
Neural networks are inspired by the human brain
Python is a popular programming language for data science
TensorFlow makes building models easy and efficient
I love coding and building new things
The sun rises in the east and sets in the west
Machine learning models require data to learn patterns
Recurrent neural networks are good for sequence data"""

tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in data.split('\n'):
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

# Pad sequences
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

# Create predictors and label
xs, labels = input_sequences[:,:-1],input_sequences[:,-1]
ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)

# --- 2. Model Architecture ---

model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))
model.add(LSTM(150))
model.add(Dense(total_words, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

# --- 3. Training ---

print("Training model...")
model.fit(xs, ys, epochs=100, verbose=0)
print("Training complete.")

# --- 4. Text Generation Function ---

def complete_sentence(seed_text, next_words):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        
        # Predict the next word
        predicted_probs = model.predict(token_list, verbose=0)
        predicted_index = np.argmax(predicted_probs, axis=-1)[0]
        
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

# --- 5. Test ---

test_sentences = [
    "The quick brown",
    "Artificial intelligence",
    "Neural networks",
    "Python is"
]

print("\n--- Generated Sentences ---\n")
for seed in test_sentences:
    completed = complete_sentence(seed, 5)
    print(f"Input: '{seed}' -> Output: '{completed}'")
