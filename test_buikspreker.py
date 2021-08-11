from buikspreker import translate

def test_translate_één () : 
    assert translate(1) == "één"

def test_translate_twee () :
    assert translate (2) == "twee"

def test_translate_veertien () :
    assert translate (14) == "veertien"

    