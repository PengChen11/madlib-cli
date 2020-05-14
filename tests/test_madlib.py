from madlib_cli import __version__
from madlib_cli.madlib import *
from textwrap import dedent

def test_version():
    assert __version__ == '0.1.0'

def test_1():
    expected = True
    actual = bool(read_template('template1.txt'))
    assert expected == actual

# dedent doesn't work, why??
def test_2():
    expected = [
'''Dear Mr. and Mrs. {0[funny_first_name]} {0[weird_last_name]},

Will you let me marry your {0[something_belongs_to_someone]}? Ever since I have laid my eyes on your {0[something_belongs_to_someone]}, I have terribly fall in love with her. I wish that she will be the precious {0[funny_item]} of my life and that someday we will stay together {0[adverb_related_to_emotions]} ever after. I have a job as a/an {0[weird_occupation]} that pays ${0[integer]} each month. I promise to treat your {0[something_belongs_to_someone]} with kindness and respect.

Sincerely,
{0[weird_first_name]} {0[funny_last_name]}''',
    ['funny_first_name', 'weird_last_name', 'something_belongs_to_someone', 'something_belongs_to_someone', 'funny_item', 'adverb_related_to_emotions', 'weird_occupation', 'integer', 'something_belongs_to_someone', 'weird_first_name', 'funny_last_name']
    ]
    actual = parse('template1.txt')
    assert expected == actual


def test_3():
    actual = merge('template2.txt', ['plural_noun_representing_living_things','place','noun','plural_noun_representing_living_things_again','another_noun','adjective','verb','number','another_adjective','body_part','another_verb'],['pigs','Howaii','apple','birds','banana','weird','attack','10','terrible','lips','hurt'])

    expected ='''Two pigs, both alike in dignity,
In fair Howaii, where we lay our scene,
From ancient apple break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross`d birds take their life;
Whole misadventured piteous overthrows
Do with their banana bury their parents` strife.
The fearful passage of their weird love,
And the continuance of their parents` rage,
Which, but their children`s end, nought could attack,
Is now the 10 hours` traffic of our stage;
The which if you with terrible lips attend,
What here shall hurt'''
    assert expected==actual
