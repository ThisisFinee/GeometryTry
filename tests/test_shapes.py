import math
import pytest

from app.shapes.circle import Circle
from app.shapes.triangle import Triangle

class TestCircle:
    def test_area(self):
        c = Circle(radius=3)
        assert math.isclose(c.area(), math.pi * 9)

    def test_specific_check(self):
        c = Circle(radius=1)
        assert c.specific_shape_check() == {'is_specific': False, 'text': 'Valid circle'}

class TestTriangle:
    def test_area_known(self):
        t = Triangle(a=3, b=4, c=5)
        assert math.isclose(t.area(), 6.0)

    @pytest.mark.parametrize("sides, expected", [
        ((3, 4, 5), {'is_specific': True, 'text': "It's a right-anled triangle"}),
        ((5, 5, 6), {'is_specific': False, 'text': "It's not a right-anled triangle"})
    ])
    def test_specific_check(self, sides, expected):
        t = Triangle(a=sides[0], b=sides[1], c=sides[2])
        assert t.specific_shape_check() == expected