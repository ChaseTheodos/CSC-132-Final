#!/bin/sh

xinput --set-prop 'raspberrypi-ts' 'Coordinate Transformation Matrix' 0 1 0 -1 0 1 0 0 1 && /home/pi/CSC132-Final/default_gui.py
