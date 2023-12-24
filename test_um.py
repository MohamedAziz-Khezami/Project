from um import count


def test_count():
    assert count("um") ==1
    assert count("um hello ladies and gentelmen, um, hi")==2
    assert count("Um , Um, hello")==2
    assert count("my favorite Album is um idk")==1