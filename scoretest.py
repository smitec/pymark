import unittest

class ScoreTest(unittest.TestCase):
    score = 0
    maxScore = 0

    def add_on_success(score=0):
        def run_and_update(function):
            def run_without_args(self):
                self.__class__.maxScore += score
                function(self)
                self.__class__.score += score
            return run_without_args
        return run_and_update

    @classmethod
    def setUpClass(cls):
        cls.score = 0
        cls.maxScore = 0
    
    @classmethod
    def tearDownClass(cls):
        print("\t" + cls.__name__ + ":[" + str(cls.score) + "/"
                + str(cls.maxScore) +"]")

