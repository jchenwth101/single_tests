from unittest import TestCase
import unittest
import random
from credit_card_validator import credit_card_validator


class TestCredCardNumber(TestCase):
    def test_random_length16(self):
        for x in range(0, 100):
            random_val = random.randint(1000000000000000, 9999999999999999)
            subs_card = [int(d) for d in str(random_val)]
            cc_list = subs_card
            cc_list = [str(i) for i in cc_list]
            cc_num = int("".join(cc_list))
            credit_card_validator(str(cc_num))

if __name__ == '__main__':
    unittest.main(verbosity=2)

