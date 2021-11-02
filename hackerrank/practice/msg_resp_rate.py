# <-- EXPAND to see the data classes
import fileinput
import math


class Message:
    def __init__(self, sender, recipient, conversation_id):
        self.sender = sender
        self.recipient = recipient
        self.conversation_id = conversation_id


"""
    Sample Input:
        biz_owner_id: 42
        all_messages: [
            {"sender": 1,  "recipient": 42, "conversation_id": 1},
            {"sender": 42, "recipient": 1,  "conversation_id": 1},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 2,  "recipient": 42, "conversation_id": 2},
            {"sender": 3,  "recipient": 88, "conversation_id": 3},
            {"sender": 3,  "recipient": 42, "conversation_id": 4},
        ]

    Sample Output:
        33 (Business owner 42 received three conversations total (1, 2, and 4), but only
        responded to one conversation (conversation ID 1)).
"""


# floor(# conversations where business owner wrote >= 1 message) / (# total conversations a business owner is involved in) * 100)
def business_responsiveness_rate(biz_owner_id, all_messages):
    bizOwnerConversations = set()
    bizOwnerResponded = set()
    for message in all_messages:
        if biz_owner_id == message.sender:
            bizOwnerResponded.add(message.conversation_id)
            bizOwnerConversations.add(message.conversation_id)
        elif biz_owner_id == message.recipient:
            bizOwnerConversations.add(message.conversation_id)
    if len(bizOwnerConversations) == 0:
        return 0
    # print("bizMessg: {}".format(len(bizOwnerResponded)))
    # print("uniq bizConversations: {}".format(len(bizOwnerConversations)))
    return math.floor(len(bizOwnerResponded) / len(bizOwnerConversations) * 100)


if __name__ == '__main__':

    lines = list(fileinput.input())
    biz_owner_id = lines[0].rstrip()

    all_messages = []
    for line in lines[1:]:
        if not line:
            break
        sender, recipient, conversation_id = line.split(' ')
        all_messages.append(
            Message(
                sender,
                recipient,
                conversation_id.rstrip(),
            ),
        )

    print(business_responsiveness_rate(biz_owner_id, all_messages))
