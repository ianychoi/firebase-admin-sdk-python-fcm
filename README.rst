Firebase: Admin SDK (Python) + FCM
++++++++++++++++++++++++++++++++++

This repository is intended to illustrate how to execute `Firebase Admin SDK
<https://firebase.google.com/docs/admin/setup>`_ to send FCM messages to a
specific iOS or Android device.

Usage
=====

* Install ``firebase-admin`` `PyPI <https://pypi.org>`_ library.
  Using a virtual environment such as `venv <https://docs.python.org/3/library/venv.html>`_
  or `virtualenv <https://virtualenv.pypa.io/en/stable/>`_ is encouraged.

  .. code::
    $ pip install firebase-admin

* Download a JSON file from Firebase admin page.
  An example of file names is: ``fcmtest-*-firebase-adminsdk-*-*.json``.

* Execute a sample `fcm-test.py <fcm-test.py>`_ file. You may need to edit:

 * ``[downloaded_certificate].json``: Downloaded JSON file
 * ``[fcm_device_registration_token]``: Device FCM registration token.

* You can also change a sample JSON message for a target device.
