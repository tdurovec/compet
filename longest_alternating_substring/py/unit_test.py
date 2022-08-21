import unittest
from program import longest_substring

class TestStringMethods(unittest.TestCase):

    def test_validation(self):

        self.assertEqual(longest_substring("844929328912985315632725682153"), "56327256")
        self.assertEqual(longest_substring("769697538272129475593767931733"), "27212947")
        self.assertEqual(longest_substring("937948289456111258444958189244"), "894561")
        self.assertEqual(longest_substring("736237766362158694825822899262"), "636")
        self.assertEqual(longest_substring("369715978955362655737322836233"), "369")
        self.assertEqual(longest_substring("345724969853525333273796592356"), "496985")
        self.assertEqual(longest_substring("548915548581127334254139969136"), "8581")
        self.assertEqual(longest_substring("417922164857852157775176959188"), "78521")
        self.assertEqual(longest_substring("251346385699223913113161144327"), "638569")
        self.assertEqual(longest_substring("483563951878576456268539849244"), "18785")
        self.assertEqual(longest_substring("853667717122615664748443484823"), "474")
        self.assertEqual(longest_substring("398785511683322662883368457392"), "98785")
        self.assertEqual(longest_substring("368293545763611759335443678239"), "76361")
        self.assertEqual(longest_substring("775195358448494712934755311372"), "4947")
        self.assertEqual(longest_substring("646113733929969155976523363762"), "76523")

if __name__ == '__main__':
    unittest.main()
