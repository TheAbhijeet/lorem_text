==========
Lorem Text
==========


.. image:: https://travis-ci.org/TheAbhijeet/lorem_text.svg?branch=master
        :target: https://travis-ci.org/TheAbhijeet/lorem_text

.. image:: https://readthedocs.org/projects/lorem-text/badge/?version=latest
        :target: https://lorem-text.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Dummy lorem ipsum text generator 


* Free software: MIT license
* Documentation: https://lorem-text.readthedocs.io.


Features
--------
Dummy lorem ipsum text generator for Python.

* Generate dummy senetnce, paragraphs and words.
* Command line interface tool included.

=====
Usage
=====

To install Lorem Text, run this command in your terminal::

        pip install lorem-text


To use Lorem Text in a project::

    from lorem_text import lorem


For randomly generated sentence of lorem ipsum text where the first word is capitalized, and the sentence ends in either a period or question mark::

    lorem.sentence()

Generate a single paragraph:: 

    lorem.paragraph()


Generate multiple paragraphs of lorem ipsum text each paragraph's consists of 2 to 4 sentences::

    paragraph_length = 5
    lorem.paragraphs(paragraph_length)


Generate random lorem ipsum words seperated with single space::

    words = 10
    lorem.words(words)


Command Line Interface 
----------------------

For randomly generated paragraph of lorem ipsum text::

    lorem_text

Lorem ipsum sentence::

    lorem_text --s 

Lorem ipsum words::

    lorem_text --words=50

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
