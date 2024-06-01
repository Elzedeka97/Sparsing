#pylint: disable=missing-docstring
import pytest

from src.parse import get_info

@pytest.fixture()
def file_parse(tmpdir):
    filename = "data.txt"
    filename = tmpdir.join(filename)
    with open(filename, "w", encoding="utf-8") as file_:
        file_.write("""Denis ; Elzedeka97
Vadim ; Vadim97
""")
    return filename

@pytest.fixture()
def file_parse_wrong(tmpdir):
    filename = "data_wrong.txt"
    filename = tmpdir.join(filename)
    with open(filename, "w", encoding="utf-8") as file_:
        file_.write("""Denis ; testuser
Vadim ; Vadim97
""")
    return filename

def test_parse(file_parse):
    sh_ans = [{'name': 'Denis', 'login': 'Elzedeka97'},
              {'name': 'Vadim', 'login': 'Vadim97'}]
    ans = get_info(file_parse)

    assert ans == sh_ans

def test_parse_wrong(file_parse_wrong):
    with pytest.raises(RuntimeError):
        ans = get_info(file_parse_wrong)
