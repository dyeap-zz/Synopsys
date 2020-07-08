# Below is the unit test for the three different implementation of finding and storing neighbors
# A - easiest and quickest function to understand solution
# B - fewest number of python line solution
# C - fewest memory usage solution

import unittest
from FindNeighbors import easily_understood, fewest_lines, fewest_memory
class TestNei(unittest.TestCase):
    def test1(self):
        # setup
        nums = []
        expectedRes  = []
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a,expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test2(self):
        # setup
        nums = [1]
        expectedRes = []
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test3(self):
        # setup
        nums = [1,2]
        expectedRes = [(2,1)]
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test4(self):
        # setup
        nums = [1,2,1]
        expectedRes = [(2,1),(1,2)]
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test5(self):
        # setup
        nums = [1,2,1,2]
        expectedRes = [(2,1),(1,2),(2,1)]
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test6(self):
        # setup
        nums = [1,3,5,7]
        expectedRes = [(3,1),(5,3),(7,5)]
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test7(self):
        # setup
        nums = [1,"3"]
        expectedRes = [("3",1)]
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test7(self):
        # setup
        nums = [1,4.4]
        expectedRes = [(4.4,1)]
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test7(self):
        # setup
        li_dummy = [1,2]
        nums = [1,li_dummy]
        expectedRes = [(li_dummy,1)]
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test7(self):
        # setup
        li_dummy = (1,2)
        nums = [1,li_dummy]
        expectedRes = [(li_dummy,1)]
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

    def test8(self):
        # setup
        li_dummy = (1,2)
        nums = [1,li_dummy,"3"]
        expectedRes = [(li_dummy,1),("3",li_dummy)]
        # run
        res_a = easily_understood(nums)
        res_b = fewest_lines(nums)
        res_c = fewest_memory(nums)
        # test
        self.assertEqual(res_a, expectedRes)
        self.assertEqual(res_b, expectedRes)
        self.assertEqual(res_c, expectedRes)

if __name__ == '__main__':
    unittest.main()
