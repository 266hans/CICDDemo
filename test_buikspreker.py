from buikspreker import translate

def test_translate_één () : 
    assert translate(1) == "één"

def test_translate_twee () :
    assert translate (2) == "twee"

def test_translate_veertien () :
    assert translate (14) == "veertien"

def test_translate_vijftien () :
    assert translate (15) == "vijftien"

def test_translate_zestien () :
    assert translate (16) == "zestien"

def test_translate_hogere_getallen () :
    assert translate (18) == "achttien"
    assert translate (19) == "negentien"
    assert translate (17) == "zeventien"
