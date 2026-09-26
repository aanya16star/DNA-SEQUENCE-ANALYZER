from validation import is_valid_dna
from analysis import count_nucleotides, gc_content
from genetics import complementary_strand


def test_validation():
    assert is_valid_dna("ATGC") is True
    assert is_valid_dna("ATGX") is False
    assert is_valid_dna("") is False


def test_count():
    result = count_nucleotides("ATGC")
    assert result["A"] == 1
    assert result["T"] == 1
    assert result["G"] == 1
    assert result["C"] == 1


def test_gc_content():
    assert gc_content("ATGC") == 50.0


def test_complement():
    assert complementary_strand("ATGC") == "TACG"


if __name__ == "__main__":
    test_validation()
    test_count()
    test_gc_content()
    test_complement()
    print("All basic tests passed.")
