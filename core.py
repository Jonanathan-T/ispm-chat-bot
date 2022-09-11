import ampalibe
from ampalibe import webserver

chat = ampalibe.Messenger()

# create a get started option to get permission of user.
# chat.get_started()


@webserver.get('/hello')
def test():
    return 'Hello, test'


@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    '''
    main function where messages received on
    the facebook page come in.

    @param sender_id String: 
        sender facebook id
    @param cmd String: 
        message content
    @param extends Dict: 
        contain list of others
            data sent by facebook (sending time, ...)
            data sent by your payload if not set in parameter
    '''

    chat.send_message(sender_id, "Hello, Ampalibe")
