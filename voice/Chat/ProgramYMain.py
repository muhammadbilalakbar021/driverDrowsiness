from programy.clients.embed.basic import EmbeddedBasicBot
from programy.clients.embed.datafile import EmbeddedDataFileBot

files = {'aiml': ['Chat/files/aiml']}

my_bot = EmbeddedBasicBot()

# print("Response = %s" % my_bot.ask_question("Hello"))
# msg = input("Me: ")
# while msg:
#     if msg == 'quit' or msg == 'exit':
#         break
#     # if my_bot.ask_question(msg) == "You aren't making sense to me...":
#     #     print("In Bot Brain")
#     #     my_bot = EmbeddedBasicBot()
#     #     my_bot.ask_question(msg)
#     #     print("Response = %s" % my_bot.ask_question(msg))
#
#     print("Response = %s" % my_bot.ask_question(msg))
#     msg = input("Me: ")


def ChatBot(input_text):
    print(input_text)
    a=my_bot.ask_question(input_text)
    print(a)
    return a
