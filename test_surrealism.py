import surrealism as s
import unittest
import random
import sys


class SurrealismUnittests(unittest.TestCase):
    """getsentence() unittests"""

    def setUp(self):
        self.variable_types = ''

        if sys.version_info[0] < 3:
            # noinspection PyUnresolvedReferences
            self.variable_types = (unicode, str)
        else:
            self.variable_types = str

    def tearDown(self):
        self.variable_types = ''
        pass

    def test_showsentences_returns_a_list(self):
        sentence_list = s.showsentences()
        self.assertIsInstance(sentence_list, list)

    def test_showsentences_returns_a_list_of_tuples(self):
        sentence_list = s.showsentences()
        for tup in sentence_list:
            self.assertIsInstance(tup, tuple)

    def test_sentencetest_does_something(self):
        sentence_list = s.sentencetest()
        self.assertIsInstance(sentence_list, list)

    def test_sentencetest_returns_a_list_of_tuples(self):
        sentence_list = s.sentencetest()
        for tup in sentence_list:
            self.assertIsInstance(tup, tuple)

    def test_getsentence_returns_a_unicode_string(self):
        sentence = s.getsentence()
        self.assertIsInstance(sentence, self.variable_types)

    def test_getsentence_returns_a_unicode_string_with_integer_upper_limit(self):
        limits = s.__gettablelimits__()
        upper_limit = limits['max_sen']
        sentence = s.getsentence(upper_limit)
        self.assertIsInstance(sentence, self.variable_types)

    def test_getsentence_returns_a_unicode_string_with_integer_lower_limit(self):
        lower_limit = 1
        sentence = s.getsentence(lower_limit)
        self.assertIsInstance(sentence, self.variable_types)

    def test_getsentence_with_a_random_integer(self):
        limits = s.__gettablelimits__()
        upper_sentence_limit = limits['max_sen']
        sen_id = random.randint(1, upper_sentence_limit)
        sentence = s.getsentence(sen_id)
        self.assertIsInstance(sentence, self.variable_types)

    def test_getsentence_returns_a_unicode_string_over_integer_upper_limit(self):
        limits = s.__gettablelimits__()
        over_limit = limits['max_sen'] + 1
        self.assertRaises(TypeError, (s.getsentence(over_limit)))

    def test_getsentence_returns_an_error_when_we_submit_a_string(self):
        _string = 'hello my name is bob'
        self.assertRaises(TypeError, (s.getsentence(_string)))

    def test_getsentence_returns_an_error_when_we_submit_a_number_as_a_string(self):
        _string = '64'
        self.assertRaises(TypeError, (s.getsentence(_string)))

    def test_getsentence_returns_an_error_when_we_submit_a_negative_number(self):
        _number = -1
        self.assertRaises(TypeError, (s.getsentence(_number)))

    def test_getsentence_handles_it_when_we_submit_a_float(self):
        _number = 98.9
        sentence = s.getsentence(_number)
        print(sentence)
        self.assertIsInstance(sentence, self.variable_types)

    def test_that_no_hashed_keywords_remain_in_sentence(self):
        keywords = ['#VERB', '#NOUN', '#ADJECTIVE', '#NAME',
                    '#ADJECTIVE_MAYBE', '#AN', '#RANDOM', '#CAPITALISE', '#CAPALL']
        sentence = s.getsentence()
        for keyword in keywords:
            self.assertNotIn(keyword, sentence)

    def test_that_repeating_elements_actually_are_replaced(self):
        _number = 47
        sentence = s.getsentence(_number)
        self.assertIsInstance(sentence, self.variable_types)
        keywords = ['#REPEAT', '#DEFINE_REPEAT']
        sentence = s.getsentence()
        for keyword in keywords:
            self.assertNotIn(keyword, sentence)

    # noinspection PyStatementEffect
    """getfault() unit tests"""

    def test_showfaults_returns_a_list(self):
        fault_list = s.showfaults()
        self.assertIsInstance(fault_list, list)

    def test_showfaults_returns_a_list_of_tuples(self):
        fault_list = s.showfaults()
        for tup in fault_list:
            self.assertIsInstance(tup, tuple)

    def test_faulttest_returns_a_list(self):
        fault_list = s.faulttest()
        self.assertIsInstance(fault_list, list)

    def test_faulttest_returns_a_list_of_tuples(self):
        fault_list = s.faulttest()
        for tup in fault_list:
            self.assertIsInstance(tup, tuple)

    def test_getfault_returns_a_unicode_string(self):
        fault = s.getfault()
        self.assertIsInstance(fault, self.variable_types)

    def test_getfault_returns_a_unicode_string_with_integer_upper_limit(self):
        limits = s.__gettablelimits__()
        upper_limit = limits['max_fau']
        fault = s.getfault(upper_limit)
        self.assertIsInstance(fault, self.variable_types)

    def test_getfault_returns_a_unicode_string_with_integer_lower_limit(self):
        lower_limit = 1
        fault = s.getfault(lower_limit)
        self.assertIsInstance(fault, self.variable_types)

    def test_getfault_with_a_random_integer(self):
        limits = s.__gettablelimits__()
        upper_fault_limit = limits['max_fau']
        fau_id = random.randint(1, upper_fault_limit)
        fault = s.getfault(fau_id)
        self.assertIsInstance(fault, self.variable_types)

    def test_getfault_returns_a_unicode_string_over_integer_upper_limit(self):
        limits = s.__gettablelimits__()
        over_limit = limits['max_fau'] + 1
        self.assertRaises(TypeError, (s.getsentence(over_limit)))

    def test_getfault_returns_an_error_when_we_submit_a_string(self):
        _string = 'hello my name is bob'
        self.assertRaises(TypeError, (s.getfault(_string)))

    def test_getfault_returns_an_error_when_we_submit_a_number_as_a_string(self):
        _string = '64'
        self.assertRaises(TypeError, (s.getfault(_string)))

    def test_getfault_returns_an_error_when_we_submit_a_negative_number(self):
        _number = -1
        self.assertRaises(TypeError, (s.getfault(_number)))

    def test_getfault_handles_it_when_we_submit_a_float(self):
        _number = 98.9
        fault = s.getfault(_number)
        print(fault)
        self.assertIsInstance(fault, self.variable_types)

    def test_that_no_hashed_keywords_remain_in_fault(self):
        keywords = ['#VERB', '#NOUN', '#ADJECTIVE', '#NAME',
                    '#ADJECTIVE_MAYBE', '#AN', '#RANDOM', '#CAPITALISE', '#CAPALL']
        fault = s.getfault()
        for keyword in keywords:
            self.assertNotIn(keyword, fault) 