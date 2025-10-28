import pytest

from palindromes.core import p1, p2


@pytest.mark.parametrize("func", [p1, p2])
class TestPalindromes:
    def test_empty(self, func) -> None:
        assert func("") == {""}

    def test_panama(self, func) -> None:
        assert func("A man, a plan, a canal, Panama!") == {"amanaplanacanalpanama"}

    def test_dennis_and_edna(self, func) -> None:
        assert func("Dennis and Edna sinned!") == {"dennisandednasinned"}

    def test_wooloomooloo(self, func) -> None:
        # See https://en.wikipedia.org/wiki/Woolloomooloo
        assert func("Wooloomooloo") == {"ooloomooloo"}

    def test_equal_length_palindromes(self, func) -> None:
        assert func("jack ca son os") == {"ackca", "sonos"}

    def test_a_kook_in_the_afternoon(self, func) -> None:
        assert func("A saw a kook this afternoon") == {"kook", "noon"}

    def test_two_kooks_around_noon(self, func) -> None:
        assert func("A saw a kook before noon, then another kook") == {"kook", "noon"}

    def test_a_kookaburra(self, func) -> None:
        assert func("A saw a kookaburra!") == {"akooka"}

    def test_leonie_meiners(self, func) -> None:
        assert func("Leonie Meiners") == {"niemein"}

    def test_till_best(self, func) -> None:
        assert func("Till Best") == {"ll"}

    def test_tiina_mauno(self, func) -> None:
        assert func("Tiina Mauno") == {"ama"}

    def test_jackson_emanuel(self, func) -> None:
        assert func("Jackson Emanuel") == set("acejklmnosu")
