from jaraco.parables import text_gen
from jaraco.parables.config import config


def test_missing_phrase(tmp_path, capsys):
    path = tmp_path / 'phrases.txt'
    path.write_text('[phrases]\nstarter : {missing}\n', encoding='utf-8')
    assert config(str(path)).get_phrase('missing') == ''
    assert 'Could not find phrases with key missing' in capsys.readouterr().out


def test_gen_phrases(capsys):
    path = text_gen.direct_or_package_file('self-reference')
    text_gen.gen_phrases(path, 2)
    lines = capsys.readouterr().out.splitlines()
    assert lines[-1] and lines[-2]
