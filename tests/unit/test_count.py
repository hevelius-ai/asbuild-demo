from app.count import count_words


def test_counts_words_across_lines(tmp_path):
    f = tmp_path / "a.txt"
    f.write_text("one  two\n\tthree\n")
    assert count_words(str(f)) == 3


def test_empty_file_has_no_words(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("")
    assert count_words(str(f)) == 0
