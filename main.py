import os
import json
from typing import List, Tuple
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class EmailClassifier:
    """
    A utility for classifying emails based on their content.
    """

    def __init__(self, data_dir: str):
        """
        Initialize the utility with the directory containing the email data.

        :param data_dir: The directory containing the email data.
        """
        self.data_dir = data_dir
        self.classifier = None

    def load_data(self) -> Tuple[List[str], List[str]]:
        """
        Load the email data from the data directory.

        :return: A tuple containing two lists: the email contents and their corresponding labels.
        """
        contents = []
        labels = []
        for filename in os.listdir(self.data_dir):
            with open(os.path.join(self.data_dir, filename), 'r') as f:
                email = json.load(f)
                contents.append(email['content'])
                labels.append(email['label'])
        return contents, labels

    def train(self, test_size: float = 0.2):
        """
        Train the email classifier.

        :param test_size: The proportion of the data to use as a test set.
        """
        contents, labels = self.load_data()
        contents_train, contents_test, labels_train, labels_test = train_test_split(contents, labels, test_size=test_size)

        self.classifier = Pipeline([
            ('vectorizer', CountVectorizer(tokenizer=word_tokenize, stop_words=stopwords.words('english'))),
            ('classifier', MultinomialNB())
        ])

        self.classifier.fit(contents_train, labels_train)

        labels_pred = self.classifier.predict(contents_test)
        print(f'Accuracy: {accuracy_score(labels_test, labels_pred)}')

    def classify(self, content: str) -> str:
        """
        Classify an email based on its content.

        :param content: The content of the email.
        :return: The label of the email.
        """
        if self.classifier is None:
            raise Exception('The classifier has not been trained yet.')
        return self.classifier.predict([content])[0]


# Example usage:
classifier = EmailClassifier('email_data')
classifier.train()
print(classifier.classify('Congratulations, you have won a prize!'))