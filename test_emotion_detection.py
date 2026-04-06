import unittest
from EmotionDetection.emotion_detection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        r = emotion_detection( 'I am glad this happened')
        self.assertEqual( r['dominant_emotion'], 'joy')

        r = emotion_detection( 'I am really mad about this')
        self.assertEqual( r['dominant_emotion'], 'anger')

        r = emotion_detection( 'I feel disgusted just hearing about this')
        self.assertEqual( r['dominant_emotion'], 'disgust')

        r = emotion_detection( 'I am so sad about this')
        self.assertEqual( r['dominant_emotion'], 'sadness')

        r = emotion_detection( 'I am really afraid that this will happen')
        self.assertEqual( r['dominant_emotion'], 'fear')
        

unittest.main()