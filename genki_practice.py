# For working with the genki csv
import pandas as pd
import nouns

# Pick random nouns, verbs, etc.
from random import choice as pick

# Automatic verb conjugation, sort of
from japaneseverbconjugator.src import JapaneseVerbFormGenerator
from japaneseverbconjugator.src.constants.EnumeratedTypes import (
    VerbClass,
    Tense,
    Polarity,
)

jvfg = JapaneseVerbFormGenerator.JapaneseVerbFormGenerator()

# ================================================================== #
# The provided macros are too verbose for me
#
# Requires: verb, verb_class, tense, polarity
plain_form = jvfg.generate_plain_form

# Requires: verb, verb_class
te_form = jvfg.generate_te_form

# たい form. Requires: verb, verb_class, formality, polarity
volitional_form = jvfg.generate_volitional_form
# ------------------------------------------------------------------ #


# Row 9 in the column name row
df = pd.read_excel("Genki_2.xlsx", header=9)

# The columns have names written in japanese. I'm not going to mutate
# the csv in any way so we'll just rename the columns of the dataframe
# as we instantiate it.
#
# "pos" is for "part of speech"
c = {"単語": "word", "漢字表記": "kanji", "品詞": "pos", "英訳": "english", "課数": "lesson"}
df.rename(columns=c, inplace=True)


# Replace the "parts of speech" entries with easier labels.
#
# Yes, they're longer (for the most part), but it's just easier to
# read in-place so whatever.
parts_of_speech = {
    "n.": "noun",  # noun
    "い-adj.": "i-adj",  # i adjective
    "な-adj.": "na-adj",  # na adjective
    "u-v.": "u-verb",  # u verb
    "ru-v.": "ru-verb",  # ru verb
    "irr-v.": "irr-verb",  # irregular verb
    "adv.": "adv",  # adverb --- abbreviate so can filter by "verb" in
    "part.": "particle",  # particle
    "pre.": "pre-nom",  # pre-nominal expression, e.g. 「その___」
    "suf.": "nf-suffix",  # (noun-forming) suffix, e.g. 「___円」or「___か月」
    "exp.": "expression",  # expression
}

# Replace the columns
df["pos"].replace(parts_of_speech, inplace=True)


def filter_by(df, col, val):
    """
    df: the genki csv dataframe
    col: the column we want to filter in
    val: the value we want to filter for

    Example:
        filter_by(df, "lesson", "L15")

    We have to do this because pandas built-in filtering scheme
    doesn't allow us to filter by things like `val in df[col]`, so we
    can't do things like `"L11" in df[col]` because the columns are
    formatted like "会L11-II" or something.
    """
    # If we passed in a list of values to filter by, we check for
    # where _any_ of them are valid
    if type(val) == list:
        return df[
            [any([val_entry in df_entry for val_entry in val]) for df_entry in df[col]]
        ]

    # Create a simple bool array to index into the dataframe with
    return df[[val in entry for entry in df[col]]]


# Get vocab for lessons 3-12. We have to get vocab for lessons 1 and 2
# separately because the "in" part messes up by including things from
# L11, L12, L13, ... because they all contain L1.
#
# I guess I should have just hard-coded this from the beginning but
# w/e.
our_lessons = [f"L{i}" for i in range(3, 13)]
df = filter_by(df, "lesson", our_lessons)
l1df = df[[("会L1" == entry) or ("L1," in entry) for entry in df["lesson"]]]
l2df = df[[("会L2" == entry) or ("L2," in entry) for entry in df["lesson"]]]
df = pd.concat([df, l1df, l2df])

# Define an easy-access list of verbs
verb_df = filter_by(df, "pos", "verb")
verb_list = [entry for entry in verb_df["english"]]


def write_nouns():
    """
    write nouns to a text file so that we can do stuff with them
    """
    text_file = open("Nouns.txt", "w")
    n_df = filter_by(df, "pos", "noun")
    noun_string = ""
    for noun in n_df["english"].values:
        noun_string += f'"{noun}",\n'
    text_file.write(noun_string)
    text_file.close


def verb_to_verbing(verb):
    """
    convert an english verb to "ing" form, or at least try to.
    """
    if verb[0:3] == "to ":
        verb = verb[3:]
    # print(verb)
    index = verb.find(" ", 0, len(verb))

    if index == -1:
        if verb[index] == "e":
            return verb[:index] + "ing"
        else:
            return verb + "ing"
    else:
        if verb[index] == "e":
            verb = verb[0:index] + verb[index + 1 :]

    return verb[0:index] + "ing" + verb[index:]


def verb_class(en_verb):
    verb = df[[en_verb == entry for entry in df["english"]]]
    verb_class = verb["pos"].values[0]
    if verb_class == "ru-verb":
        return VerbClass.ICHIDAN
    elif verb_class == "u-verb":
        return VerbClass.GODAN
    elif verb_class == "irr-verb":
        return VerbClass.IRREGULAR
    else:
        assert False  # Haha what


def japanese(english):
    """
    return the japanese word corresponding to the `english` entry in
    our dataframe. Must be the exact wording given in the textbook.
    """
    row = df[[english == entry for entry in df["english"]]]
    return row["word"].values[0]


def english(japanese):
    """
    return the japanese word corresponding to the `english` entry in
    our dataframe. Must be the exact wording given in the textbook.
    """
    row = df[[japanese == entry for entry in df["word"]]]
    return row["word"].values[0]


# ================================================================== #
#                                                                    #
#                        Ok now the real shit                        #
#                                                                    #
# ================================================================== #
#                                                                    #
#                      (i.e. practice functions)                     #
#                                                                    #
# ------------------------------------------------------------------ #


def qualify_noun():
    """
    Qualifying nouns with verbs and adjectives (see: L9, pg. 213-214)
    """
    # The method by which we'll indicate who is the subject of our
    # sentence. These crrespond to the 4 examples given on page 214.
    options = ["place", "frequency", "verb", "time"]
    option = pick(options)

    # Pick the verb
    verb = "it"
    while ("(something)" in verb) or (
        verb[0:2] == "it"
    ):  # don't want verbs like "はじまる"
        verb = pick(verb_list)

    ja_verb = japanese(verb)
    vclass = verb_class(verb)

    if option == "place":
        en_verb = verb_to_verbing(verb)  # make it into the "ing" form
        ja_te_verb = te_form(ja_verb, vclass)

        english_prompt = f"The person who is [{en_verb}] over there"
        response = f"あそこで{ja_te_verb}いる人"

    elif option == "frequency":
        freq = pick(nouns.frequency)  # Get a frequency word
        jfreq = japanese(freq)  # Convert it to japanese too

        en_verb = verb[3:]  # remove the leading "to "

        english_prompt = f"People who [{en_verb}] {freq}"
        response = f"{jfreq}{ja_verb}人"

    elif option == "verb":
        (polarity, eng_pol) = pick(
            [(Polarity.POSITIVE, ""), (Polarity.NEGATIVE, "NOT")]
        )

        en_verb = verb[3:]  # remove the leading "to "
        ja_ta_verb = plain_form(ja_verb, vclass, Tense.NONPAST, polarity)
        english_prompt = f"People who do {eng_pol} [{en_verb}]"
        response = f"{ja_ta_verb}人"

    else:
        time = pick(nouns.times_past)
        jtime = japanese(time)

        en_verb = verb[3:]  # remove the leading "to "
        ja_ta_verb = plain_form(ja_verb, vclass, Tense.PAST, Polarity.POSITIVE)

        english_prompt = f"A friend who [{en_verb} (PAST)] {time}"
        response = f"{jtime}{ja_ta_verb}友だち"

    # elif option == "time":
    try:
        user_input = input("translate " + english_prompt + "\n")
    except UnicodeDecodeError:
        pass

    return response
