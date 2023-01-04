import simpleTesting
from nose.tools import *

testFile = "testFiles/test.xml"


def test_normalizeSpace():
    """ Replaces all whitespace spans with a newline character for tokenization."""
    assert_equal("", simpleTesting.normalizeSpace(" \n\n    "))
    assert_equal("\nmiddle\n", simpleTesting.normalizeSpace(" \n   middle "))
    assert_equal("start\n", simpleTesting.normalizeSpace("start \n    "))
    assert_equal("Hello,\nworld\n!", simpleTesting.normalizeSpace("Hello,\n world   !"))


def test_extract():
    assert_equal("\n<del rend=\"strikethrough\" xml:id=\"c56-0105__main__d5e22055\">\"</del>\n"
                 "\n<longToken>must\ndie\n–</longToken>\n"
                 , simpleTesting.extract(testFile))


def test_fixToken():
    """ Add space before and after dash and hyphen """
    assert_equal("This\n-\nis\n‒\na \n–\ntest \n—\nstring.", simpleTesting.fixToken("This-is‒a –test —string."))


def test_normalize():
    assert_equal("and", simpleTesting.normalize("&amp;amp;"))


def test_processToken():
    assert_dict_equal({'t': '&amp; ', 'n': 'and'}, simpleTesting.processToken("&amp;"))

def test_processWitness():
    inputWitness = ["and"]
    id = 'f1818'
    assert_dict_equal({'id': 'f1818', 'tokens': [{'n': 'and', 't': 'and '}]},
                 simpleTesting.processWitness(inputWitness, id))

def test_tokenize():
    test = open(testFile, "rb")
    assert_list_equal(['', '<del rend="strikethrough" xml:id="c56-0105__main__d5e22055">"</del>',
                  '<longToken>must', 'die', '–</longToken>', ''], simpleTesting.tokenize(test))

# def test_tokenizeFiles():
#     assert_equal("", simpleTesting.tokenizeFiles(f1818, f1823, fThomas, f1831, fMS))



