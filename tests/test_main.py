file content

import unittest
from email_classifier import EmailClassifier

class TestEmailClassifier(unittest.TestCase):

    def setUp(self):
        self.classifier = EmailClassifier('email_data')

    def test_train(self):
        self.classifier.train()
        self.assertIsNotNone(self.classifier.classifier)

    def test_classify(self):
        self.classifier.train()
        label = self.classifier.classify('Congratulations, you have won a prize!')
        self.assertIn(label, ['spam', 'ham'])

if __name__ == '__main__':
    unittest.main()