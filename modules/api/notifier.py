import boto3
from botocore.exceptions import ClientError

class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""
    def __init__(self):
        topicName = f"allinone-api-notification"

        self.sns_resource = boto3.resource('sns')

        try:
            self.sns_topic = self.sns_resource.create_topic(Name=topicName)
        except ClientError:
            raise

    @staticmethod
# snippet-start:[python.example_code.sns.Publish_Message]
    def publish_message(topic, message):
        """
        Publishes a message, with attributes, to a topic. Subscriptions can be filtered
        based on message attributes so that a subscription receives messages only
        when specified attributes are present.

        
        :param message: The message to publish.
        :param attributes: The key-value attributes to attach to the message. Values
                           must be either `str` or `bytes`.
        :param topic: The topic to publish to.
        :return: The ID of the message.
        """
        try:
            # att_dict = {}
            # for key, value in attributes.items():
            #     if isinstance(value, str):
            #         att_dict[key] = {'DataType': 'String', 'StringValue': value}
            #     elif isinstance(value, bytes):
            #         att_dict[key] = {'DataType': 'Binary', 'BinaryValue': value}
            response = topic.publish(Message=message)
            message_id = response['MessageId']
        except ClientError:
            raise
        else:
            return message_id
# snippet-end:[python.example_code.sns.Publish_Message]