"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story1 = Story(
    ["main_char", "noun", "pronoun", "present_tense_verb", "body_part", "present_tense_verb2"],
    """{main_char} was a {noun}. {pronoun} wanted to {present_tense_verb}, but could not, on account of their {body_part} injury. {main_char} lives a really tough life. {pronoun} {present_tense_verb2} 20 times everyday to cope."""
)

story2 = Story(
    ["present_tense_verb", "plural_body_part", "noun"],
    """Hi, nice to {present_tense_verb} you. I just washed my {plural_body_part} using a {noun}, so I think it will be fine if we shook {plural_body_part}."""
)

stories = [story, story1, story2]