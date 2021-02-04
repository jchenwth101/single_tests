from unittest import TestCase
import unittest
import random
from credit_card_validator import credit_card_validator


class TestCredCardNumber(TestCase):
    def test_prefix_range_mastercard(self):
        for x in range(0, 1000):
            for i in range(2221, 2721):
                cc_prefix = [int(d) for d in str(i)]
                random_val = random.randint(100000000000, 999999999999)
                subs_card = [int(d) for d in str(random_val)]
                cc_list = cc_prefix + subs_card
                cc_list = [str(i) for i in cc_list]
                cc_num = int("".join(cc_list))
                credit_card_validator(str(cc_num))

if __name__ == '__main__':
    unittest.main(verbosity=2)

