# Reef Tank Power Control

This is a quick project I put together to control an 8 channel power relay conneced to a Raspberry Pi. I plan to add support for temprature sensors, ph probes, light timers, and more. 

## Getting Started

The files in this project will get you up and running with a web based "portal" where you can toggle outlets, groups of outlets, get the status of outlets, and control other relay functions.

### Prerequisites

This app is written in Python and uses Flask. You will need a Raspberry Pi, an appropriate relay, and wiring. You can view pictures of my build [here](https://photos.app.goo.gl/66KXyf0TYG3iR5cI2).

Once setup you will need to edit my code to use the correct pins for your implementation.

I am running this app via Supervisor. To get up and running quickly, you can run:
```
python app.py
```
or

```
export FLASK_APP="app.py"
python -m flask run --host=0.0.0.0
```

