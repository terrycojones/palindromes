import pytest

from palindromes.djp import djp_1
from palindromes.nikolai import nz_1, nz_2
from palindromes.sina import st_1
from palindromes.terry import tj_1, tj_2, tj_3, tj_4


@pytest.mark.parametrize("func", [djp_1, nz_1, nz_2, st_1, tj_1, tj_2, tj_3, tj_4])
class TestPalindromes:
    def test_empty(self, func) -> None:
        assert func("") == {""}

    def test_abc(self, func) -> None:
        assert func("abc") == {"a", "b", "c"}

    def test_single_letter(self, func) -> None:
        assert func("a") == {"a"}

    def test_doubled_letter(self, func) -> None:
        assert func("aa") == {"aa"}

    def test_panama(self, func) -> None:
        assert func("A man, a plan, a canal, Panama!") == {"amanaplanacanalpanama"}

    def test_dennis_and_edna(self, func) -> None:
        assert func("Dennis and Edna sinned!") == {"dennisandednasinned"}

    def test_napoleons_lament(self, func) -> None:
        assert func("Able was I, 'ere I saw Elba :-(") == {"ablewasiereisawelba"}

    def test_wooloomooloo(self, func) -> None:
        # See https://en.wikipedia.org/wiki/Woolloomooloo
        assert func("Wooloomooloo") == {"ooloomooloo"}

    def test_equal_length_palindromes(self, func) -> None:
        assert func("jack ca son os") == {"ackca", "sonos"}

    def test_a_kook_in_the_afternoon(self, func) -> None:
        assert func("I saw a kook this afternoon") == {"kook", "noon"}

    def test_two_kooks_around_noon(self, func) -> None:
        assert func("I saw a kook before noon, then another kook") == {"kook", "noon"}

    def test_a_kookaburra(self, func) -> None:
        assert func("I saw a kookaburra!") == {"akooka"}

    def test_leonie_meiners(self, func) -> None:
        assert func("Leonie Meiners") == {"niemein"}

    def test_till_best(self, func) -> None:
        assert func("Till Best") == {"ll"}

    def test_tiina_mauno(self, func) -> None:
        assert func("Tiina Mauno") == {"ama"}

    def test_jackson_emanuel(self, func) -> None:
        assert func("Jackson Emanuel") == set("acejklmnosu")

    def test_jenny_meier(self, func) -> None:
        assert func("Jenny Meier") == {"eie"}
