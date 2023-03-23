from Reddit_ChatBot_Python import ChatBot
from Reddit_ChatBot_Python import RedditAuthentication

import configparser
config = configparser.ConfigParser()
config.read('token.ini')

reddit_authentication = RedditAuthentication.PasswordAuth(reddit_username=config['reddit']['username'],
                                                          reddit_password=config['reddit']['password'],
                                                          twofa=None)


chatbot = ChatBot(print_chat=True,
                  store_session=True,
                  log_websocket_frames=False,
                  authentication=reddit_authentication
                  )


@chatbot.event.on_ready
def report_channels(_):
    channels = chatbot.get_channels()
    my_channel = None
    for channel in channels:
        if channel.name == "My Channel":
            my_channel = channel

    last_hundred_messages = chatbot.get_older_messages(channel_url=my_channel.channel_url,
                                                       prev_limit=100)

    last_created_at = last_hundred_messages[-1].created_at
    while True:
        messages = chatbot.get_older_messages(channel_url=my_channel.channel_url,
                                              message_ts=last_created_at,
                                              prev_limit=30)
        last_created_at = messages[-1].created_at


@chatbot.event.on_ready
def check_invites(_):
    invites = chatbot.get_chat_invites()
    for invite in invites:
        print(
            f"invited to chat by {invite.inviter} with the message {invite.last_message.message}")
        chatbot.accept_chat_invite(invite.channel_url)
    return True


chatbot.run_4ever(auto_reconnect=True)
