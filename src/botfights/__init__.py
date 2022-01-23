import os
import pathlib
from typing import Optional

import fire
import pkg_resources

from botfights.wordle.wordle import get_random, load_wordlist, play_botfights, play_bots


def _gen_implementations():
    for entry_point in pkg_resources.iter_entry_points("botfights.wordle.guesser"):
        factory_func = entry_point.load()
        yield entry_point.name, factory_func


def get_implementations():
    return dict(_gen_implementations())


def wordle(
    guesser: str,
    seed: str = "",
    num: int = 0,
    event: Optional[str] = None,
    wordlist: str = "bot",
):
    get_random().seed(seed)

    wordlist = load_wordlist(wordlist)
    bot = get_implementations()[guesser](wordlist)

    if event is None:
        return play_bots({guesser: bot}, wordlist, num)
    else:
        return play_botfights(
            bot, os.environ["BOTFIGHTS_USER"], os.environ["BOTFIGHTS_PASS"], event
        )


def main():
    fire.Fire({func.__name__: func for func in [wordle]})
