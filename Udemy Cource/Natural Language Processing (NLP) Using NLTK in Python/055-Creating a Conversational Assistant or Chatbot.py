# %%
# Creating a conversational assistant or chatbot

import nltk


# %%
def built_in_engines(which_one):
    if which_one == "eliza":
        nltk.chat.eliza.demo()
    elif which_one == "iesha":
        nltk.chat.iesha.demo()
    elif which_one == "rude":
        nltk.chat.rude.demo()
    elif which_one == "suntsu":
        nltk.chat.suntsu.demo()
    elif which_one == "zen":
        nltk.chat.zen.demo()
    else:
        print("unknown built-in chat engine {}".format(which_one))


# %%
def my_engine():
    chat_pairs = (
        (r"(.*?)Stock price(.*)",
         ("Todat stock price is 100",
          "I am unable to find out the stock price.")),
          (r"(.*?)not well(.*)",
           ("Oh, tack care. May be you should visit a doctor",
            "Did you tack some medicine ?")),
            (r"(.*?)raining(.*)",
             ("It monsoon season, what more do you expect ?",
             "Yes, its good for farmers")),
             (r"How(.*?)health(.*)",
              ("I am always healthy.",
               "I am a program, super healthy!")),
               (r".*",
                ("I am good. How are you today ?",
                 "What brings you here ?"))
    )
    def chat():
        print("!" * 80)
        print(" >> my engine << ")
        print("Talk to the program using normal english")
        print("=" * 80)
        print("Enter 'quit' when done")
        chat_bot = nltk.chat.util.Chat(chat_pairs, nltk.chat.util.reflections)
        chat_bot.converse()

    chat()


# %%
if __name__ == "__main__":
    for engine in ["eliza", "iesha", "rude", "suntsu", "zen"]:
        print("=== demo of {} ===".format(engine))
        built_in_engines(engine)
        print()
    my_engine()