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
    ["verb", "plural_noun"],
    """I love to {verb} with {plural_noun}."""
)

story2 = Story(
    ["adjective", "noun", "plural_noun"],
    """I am a(n) {adjective} {noun} who collects {plural_noun}."""
)

story3 = Story(
    ["noun", "adjective", "plural_noun"],
    """Let there be {noun}, said the {adjective} {plural_noun}."""
)

story_arr = [story, story1, story2, story3]

story_select = None