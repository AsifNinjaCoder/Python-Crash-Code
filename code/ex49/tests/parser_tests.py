from nose.tools import *
from Exercise49 import lexicon
from Exercise49.parser import *

def test_peek():
    # test a single word
    word = "bear"
    lexicon_scan = lexicon.scan(word)
    word_type = peek(lexicon_scan)
    assert_equal('noun', word_type)

    # test multiple words
    words = "bear is east"
    lexicon_scan = lexicon.scan(words)
    word_type = peek(lexicon_scan)
    assert_equal('noun', word_type)

def test_match():
    # test a single word
    word = "bear"
    lexicon_scan = lexicon.scan(word)
    assert_equal("bear", match(lexicon_scan, 'noun')[1])
    assert_equal(None, match(lexicon_scan, 'noun'))

    # test multiple words
    words = "bear is east"
    lexicon_scan = lexicon.scan(words)
    assert_equal("bear", match(lexicon_scan, 'noun')[1])
    assert_equal("is", match(lexicon_scan, 'stop')[1])
    assert_equal("east", match(lexicon_scan, 'direction')[1])

def test_skip():
    # test a single word
    word = "bear"
    lexicon_scan = lexicon.scan(word)
    skip(lexicon_scan, 'verb')
    assert_equal(1, len(lexicon_scan))
    skip(lexicon_scan, 'noun')
    assert_equal(0, len(lexicon_scan))

def test_parse_subject():
    assert_equal(parse_subject([('noun', 'mountain')]), ('noun', 'mountain'))
    assert_equal(parse_subject([('verb', 'go')]), ('noun', 'player'))
    assert_raises(ParserError, parse_subject, ([('direction', 'south')]))

def test_parse_verb():
    assert_equal(parse_verb([('verb', 'walk')]), ('verb', 'walk'))
    assert_raises(ParserError, parse_verb, ([('noun', 'bear')]))

def test_parse_object():
    assert_equal(parse_object([('noun', 'house')]), ('noun', 'house'))
    assert_equal(parse_object([('direction', 'south')]), ('direction', 'south'))
    assert_raises(ParserError, parse_object, ([('verb', 'go')]))

def test_parse_sentence():
    word_list = [('verb', 'verb'), ('stop', 'stop'), ('noun', 'noun')]
    theSentence = parse_sentence(word_list)
    assert_equal(print(theSentence), print(Sentence(('noun', 'player'), ('verb', 'verb'), ('noun', 'noun'))))

def test_parse_error():
    assert_raises(ParserError, parse_sentence, ([('verb', 'walk'), ('verb', 'run')]))
    assert_raises(ParserError, parse_sentence, ([('noun', 'dog'), ('noun', 'mountain')]))
    assert_raises(ParserError, parse_sentence, ([('noun', 'person'), ('verb', 'walk'), ('verb', 'run')]))