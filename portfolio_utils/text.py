"""Text preprocessing helpers for NLP projects."""

from __future__ import annotations

import re


_URL_RE = re.compile(r"https?://\S+|www\.\S+")
_MENTION_RE = re.compile(r"@\w+")
_MULTISPACE_RE = re.compile(r"\s+")


def clean_tweet(value: object) -> str:
    """Normalize a tweet while retaining useful lexical information."""

    text = str(value).lower()
    text = _URL_RE.sub(" url ", text)
    text = _MENTION_RE.sub(" user ", text)
    text = text.replace("#", "")
    text = re.sub(r"&amp;", " and ", text)
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    return _MULTISPACE_RE.sub(" ", text).strip()
