=====
Usage
=====

To use Lorem Text in a project::

    from lorem_text import lorem


For randomly generated sentence of lorem ipsum text where The first word is capitalized, and the sentence ends in either a period or question mark::

    lorem.sentence()


To generate lorem ipsum paragraph randomly generated paragraph of lorem ipsum text.The paragraph consists of between 2 to 4 sentences::

    paragraph_length = 5
    lorem.paragraph(paragraph_length)


To generate random lorem ipsum words seperated with single space::

    words = 10
    lorem.words(words)


Command Line Interface 
--------

To generate lorem ipsum paragraph randomly generated paragraph of lorem ipsum text::

    lorem_text


For randomly generated sentence::

    lorem_text --s 


For randomly generated lorem ipsum words::

    lorem_text --words=50



