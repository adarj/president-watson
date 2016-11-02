# President Watson

Compares the personality traits of two politicians using the Watson API and Twitter.

## Requirements

This program was tested using Python 3.5; however, Python 3.4 should work as well. In order to run the program, the following modules must be installed using pip:

```
Flask
python-twitter
watson-developer-cloud
```

## Instructions

In order to start the website, you must first obtain keys for the Twitter and Watson APIs and paste them into the the `keys.ini` file located in `president_watson/app/static/api_keys/`. Afterwards, navigate to the `president_watson` directory and run the following command:

    python run.py
