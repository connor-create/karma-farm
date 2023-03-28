from .openai_config import OPENAI_KEY, MODEL

import openai

from typing import List

openai.api_key = OPENAI_KEY

concerned_citizen = " as a caring citizen"
over_the_top_person = " as a completely crazy person"
mobster = " as a mobster from the 1920's"
australian = " in a stereotypical australian accent"
sarcasm = " as a very sarcastic person"
unexpected = " with an unexpected but realistic answer"
modifier = unexpected

def reply_to_comment_chain(post_title: str, comments_in_order: List[str], override_modifier: str = "") -> str:
    # Build prompt
    if override_modifier:
        modifier_to_use = override_modifier
    else:
        modifier_to_use = modifier

    prompt = f"Reply to this as the next comment{modifier_to_use}:\n\n"
    prompt += f"Title: {post_title}\n\n"
    for comment in comments_in_order:
        prompt += f"Comment: {comment}\n\n"
    prompt += "Comment:\n\n"


    tokens = len(prompt) / 4
    if tokens > 1500:
        raise ValueError(f"post_title plus additional comments in comments_in_order is too long.  Roughly {1500 * 4} is the limit")
    tokens += 200

    response = openai.Completion.create(
        model=MODEL,
        prompt=prompt,
        temperature=0.7,
        max_tokens=int(tokens),
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0].text

def reply_to_question_post(post_title: str):
    # Build prompt
    if not post_title.endswith("?"):
        post_title += "?"
    prompt = f"Reply to this question{modifier}:\n\n"
    prompt += f"{post_title}\n\n"

    tokens = len(prompt) / 4
    tokens += 200
    if tokens > 1500:
        raise ValueError(f"post_title plus additional comments in comments_in_order is too long.  Roughly {1500 * 4} is the limit")

    response = openai.Completion.create(
        model=MODEL,
        prompt=prompt,
        temperature=0.7,
        max_tokens=int(tokens),
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0].text

def reply_to_news_post(post_title: str):
    # Build prompt
    if not post_title.endswith("?"):
        post_title += "?"
    prompt = f"Reply to this news title{modifier}:\n\n"
    prompt += f"{post_title}\n\n"

    tokens = len(prompt) / 4
    tokens += 200
    if tokens > 1500:
        raise ValueError(f"post_title plus additional comments in comments_in_order is too long.  Roughly {1500 * 4} is the limit")

    response = openai.Completion.create(
        model=MODEL,
        prompt=prompt,
        temperature=0.7,
        max_tokens=int(tokens),
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0].text

def reply_to_writing_post(post_title: str):
    # Build prompt
    if not post_title.endswith("?"):
        post_title += "?"
    prompt = f"Write a story that is less than 1000 words from this prompt:\n\"{[post_title]}\"\n\n"
    prompt += f"{post_title}\n\n"

    tokens = len(prompt) / 4
    tokens += 2000
    if tokens > 3000:
        raise ValueError(f"post_title plus additional comments in comments_in_order is too long.  Roughly {1500 * 4} is the limit")

    response = openai.Completion.create(
        model=MODEL,
        prompt=prompt,
        temperature=0.7,
        max_tokens=int(tokens),
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0].text