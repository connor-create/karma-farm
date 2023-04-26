Some scripts to automate a reddit account using gpt3 (technically any model from openai)

Install python3: https://www.python.org/downloads/

clone this repo: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

pip install praw

pip install openai

*Reddit Config*

To make a reddit account that you can automate, use these instructions to generate a script account: https://praw.readthedocs.io/en/stable/getting_started/authentication.html#password-flow
  first register an account (I recommend a brand new one) and then get the credentials generated from it in the prefs page (you will see them at the end of creating the application.

Once you have these credentials, you need to fill out the reddit_config.py with them.

CLIENT_ID = ""
SECRET = ""
USERNAME = ""
PASSWORD = ""

*OpenAI Config*

Use the openai website to create an account and get an api key.  There are usually free credits to use: https://platform.openai.com/account/api-keys

Get your openAI api key and insert it in ai/openai_config.py


From root directory, you can then run python3 reddit_event_loop.py and modify it as you see fit.
