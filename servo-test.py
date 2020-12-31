#!/usr/bin/python3

"""
    Program: Servo Motor Test Program (servo-test.py)
    Author:  M. Heidenreich, (c) 2020

    Description:

    This code is provided in support of the following YouTube tutorial:
    https://youtu.be/3tlE3fpryF0

    This program can be used to test and calibrate a servo motor
    with Raspberry Pi.

    THIS SOFTWARE AND LINKED VIDEO TOTORIAL ARE PROVIDED "AS IS" AND THE
    AUTHOR DISCLAIMS ALL WARRANTIES INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from signal import signal, SIGTERM, SIGHUP, pause
from gpiozero import Servo, Button

def safe_exit(signum, frame):
    exit(1)

servo = Servo(18, min_pulse_width=0.4/1000, max_pulse_width=2.5/1000)
left = Button(16)
right = Button(20)

try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    left.when_pressed = servo.min
    right.when_pressed = servo.max

    pause()

except KeyboardInterrupt:
    pass

finally:
    servo.close()
