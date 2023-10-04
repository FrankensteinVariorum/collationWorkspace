import collate
from nose.tools import *

testFile = "testFiles/test.xml"


def test_normalizeSpace():
    """ Replaces all whitespace spans with a newline character for tokenization."""
    assert_equal("", collate.normalizeSpace(" \n\n    "))
    assert_equal("\nmiddle\n", collate.normalizeSpace(" \n   middle "))
    assert_equal("start\n", collate.normalizeSpace("start \n    "))
    assert_equal("Hello,\nworld\n!", collate.normalizeSpace("Hello,\n world   !"))


def test_extract():
    assert_equal("\n<del rend=\"strikethrough\" xml:id=\"c56-0105__main__d5e22055\">\"</del>\n"
                 "\n<longToken>must\ndie\n–</longToken>\n"
                 , collate.extract(testFile))


def test_fixToken():
    """ Add space before and after dash and hyphen """
    assert_equal("This\n-\nis\n‒\na \n–\ntest \n—\nstring.", collate.fixToken("This-is‒a –test —string."))


def test_normalize():
    assert_equal("and", collate.normalize("&amp;amp;"))


def test_processToken():
    assert_dict_equal({'t': '&amp; ', 'n': 'and'}, collate.processToken("&amp;"))
    assert_dict_equal({'t': '“Hello world!” ', 'n':'<q>hello world!<q>'}, collate.processToken('“Hello world!”'))
    assert_dict_equal({'t': '"Hello world!" ', 'n':'<q>hello world!<q>'}, collate.processToken('"Hello world!"'))
    assert_dict_equal({'t': '"ancient ', 'n':'<q>ancient'}, collate.processToken('"ancient'))


def test_processWitness():
    inputWitness = ["and"]
    id = 'f1818'
    assert_dict_equal({'id': 'f1818', 'tokens': [{'n': 'and', 't': 'and '}]},
                 collate.processWitness(inputWitness, id))

def test_tokenize():
    test = open(testFile, "rb")
    assert_list_equal(['', '<del rend="strikethrough" xml:id="c56-0105__main__d5e22055">"</del>',
                  '<longToken>must', 'die', '–</longToken>', ''], collate.tokenize(test))

# def test_tokenizeFiles():
#     assert_equal("", collate.tokenizeFiles(f1818, f1823, fThomas, f1831, fMS))



