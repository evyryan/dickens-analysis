# Introduction

This repo is for analysis of the Dickens corpus.

TODO: Explain more about the project and what I am trying to achieve.

# How To Run

* These python notebooks are designed to be run with Python 3.11.0. To install necessary packages, run the following: 
    * `pip install -r requirements.txt`
    TODO: Explain how I set up pyenv and how I made the virtual environment

# File Organization

## Data

* Data from Project Gutenberg as plaintext (.txt file). 
    * This means there is no markup.
    * Gutenberg heading information was removed - Introductory information about Project Gutenberg, also table of contents and the prefaces.
* Each novel is named by its title.
* The directory called `canonicalNames` contains the csv files of the automatically generated (by SpacyNameFinder) for each book that I analyzed.
    * This data was copied from outputs (RawNames) and manually edited (corrected false identifications and correct names were matched to their Canonical Name).

## Notebooks

* DickensSpaceyNameFinder - iterates through the entire book and identifies all of the proper nouns. Then, outputs a .csv that has all of the proper nouns listed.

* DickensCanonicalInteractionsFinder - iterates through all the paragraphs of the book and identifies every instance where two names occur (Characters interact with each other). Outputs a .csv that has all of the interactions listed (using Canonical Names) chronologically.

* ParagraphReader - will print each paragraph so that you can check if the interactions did occur

## Outputs

* RawNames prefix = the output of DickensSpaceyNameFinder

* Interactions prefix = the output of DickensCanonicalInteractionsFinder
