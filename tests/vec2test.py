import unittest

from ..lib.vec2 import Vec2


class Vec2Test(unittest.TestCase):

    def test_add(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(3, 4)
        self.assertEqual(v1 + v2, Vec2(4, 6))

    def test_sub(self):
        v1 = Vec2(5, 6)
        v2 = Vec2(3, 4)
        self.assertEqual(v1 - v2, Vec2(2, 2))

    def test_scale(self):
        v1 = Vec2(2, 3)
        self.assertEqual(v1.scale(2), Vec2(4, 6))
        self.assertEqual(v1.scale(0.5), Vec2(1, 1.5))

    def test_eq(self):
        v1 = Vec2(2, 3)
        v2 = Vec2(2, 3)
        v3 = Vec2(3, 2)
        self.assertTrue(v1 == v2)
        self.assertFalse(v1 == v3)

    def test_ne(self):
        v1 = Vec2(2, 3)
        v2 = Vec2(3, 2)
        v3 = Vec2(2, 3)
        self.assertTrue(v1 != v2)
        self.assertFalse(v1 != v3)

    def test_lt(self):
        v1 = Vec2(1, 2)
        v2 = Vec2(2, 3)
        self.assertTrue(v1 < v2)
        self.assertFalse(v2 < v1)

    def test_gt(self):
        v1 = Vec2(3, 4)
        v2 = Vec2(2, 3)
        self.assertTrue(v1 > v2)
        self.assertFalse(v2 > v1)

    def test_le(self):
        v1 = Vec2(2, 3)
        v2 = Vec2(2, 3)
        v3 = Vec2(3, 4)
        self.assertTrue(v1 <= v2)
        self.assertTrue(v1 <= v3)
        self.assertFalse(v3 <= v1)

    def test_ge(self):
        v1 = Vec2(3, 4)
        v2 = Vec2(3, 4)
        v3 = Vec2(2, 3)
        self.assertTrue(v1 >= v2)
        self.assertTrue(v1 >= v3)
        self.assertFalse(v3 >= v1)

    def test_str(self):
        v1 = Vec2(2, 3)
        self.assertEqual(str(v1), "(2, 3)")

    def test_repr(self):
        v1 = Vec2(2, 3)
        self.assertEqual(repr(v1), "(2, 3)")


if __name__ == '__main__':
    unittest.main()
