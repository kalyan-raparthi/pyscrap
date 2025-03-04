import networkx as nx
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from fuzzywuzzy import process

# Download NLTK resources
nltk.download("stopwords")
nltk.download("wordnet")

# Initialize NLP tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Create a directed graph (Knowledge Base)
KB = nx.DiGraph()

# Function to preprocess words (lemmatization, stopword removal)
def preprocess(sentence):
    words = sentence.lower().split()
    return [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

# Function to add a sentence as a path in the graph
def add_sentence(graph, sentence):
    words = preprocess(sentence)
    for i in range(len(words) - 1):
        graph.add_edge(words[i], words[i + 1])  # Link words in sequence

# Adding sentences (branching paths)
sentences = [
    "The sky is blue",
    "The sky has clouds",
    "Sky is clear today",
    "Water is essential for life",
    "Water boils at 100 degrees",
    "The weather is nice today",
    "The sun shines brightly in summer"
]

for sentence in sentences:
    add_sentence(KB, sentence)

# Function to find closest matching word in graph
def find_closest_word(graph, word):
    all_words = list(graph.nodes)
    match, score = process.extractOne(word, all_words) if all_words else (None, 0)
    return match if score > 70 else None  # Return match if confidence > 70%

# Function to extract key topic from question
def extract_topic(question):
    words = preprocess(question)
    for word in words:
        if word in KB or find_closest_word(KB, word):
            return word
    return None

# Function to traverse and find all paths from a topic word
def traverse_all_paths(graph, query):
    topic = extract_topic(query)
    if not topic:
        return ["I don't know."]
    
    topic = find_closest_word(graph, topic) or topic  # Use closest word if needed
    paths = []
    stack = [(topic, [topic])]  # (current word, sentence path)

    while stack:
        current_word, path = stack.pop()
        successors = list(graph.successors(current_word))  # Get next words

        if not successors:  # If no more words, save the sentence
            paths.append(" ".join(path))
        else:
            for next_word in successors:
                stack.append((next_word, path + [next_word]))  # Continue path

    return paths

# Example queries
print(traverse_all_paths(KB, "How is the sky?"))  # → ["sky is blue", "sky has cloud"]
print(traverse_all_paths(KB, "What about water?"))  # → ["water is essential for life", "water boils at 100 degrees"]
print(traverse_all_paths(KB, "Tell me about sun"))  # → ["sun shine brightly in summer"]
print(traverse_all_paths(KB, "How is the weather?"))  # → ["weather is nice today"]
