import firebase_admin
from firebase_admin import credentials
import firebase_admin.messaging as messaging

cred = credentials.Certificate('[downloaded_certificate].json')
default_app = firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.
registration_token = '[fcm_device_registration_token]'

# See documentation on defining a message payload.
message = messaging.Message(
    data={
        'score': '850',
        'time': '2:45',
    },
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
