#!/usr/bin/python3

from PIL import Image, ImageTk, ImageSequence
from takePicture import *
import RPi.GPIO as GPIO
import tkinter
import time
import numPad
import os

def run_animation(image, position, speed, loop, reset):
    class Animation:
        # rpi screen resolution
        width = 480
        height = 800

        # image directory
        location = f'/home/pi/CSC132-Final/GUI/{image}.gif'

        # setup for animation
        def __init__(self, inherit):
            self.inherit = inherit
            self.canvas = tkinter.Canvas(inherit, width=Animation.width, height=Animation.height)
            self.canvas.pack()

            self.sequence = [ImageTk.PhotoImage(frame)
            for frame in ImageSequence.Iterator(Image.open(fr'{Animation.location}'))]

            self.image = self.canvas.create_image((Animation.width/2), (Animation.height/2), anchor="center", image=self.sequence[0])
            self.animate(0)

        def animate(self, frame):
            # loop animation forever
            if loop == False:
                if (frame+1) <= (len(self.sequence)):
                    self.canvas.itemconfig(self.image, image=self.sequence[frame])
                    self.inherit.after(speed, lambda: self.animate((frame+1)))
                elif reset != True:
                    Animation.pictureTime(self)
                else:
                    main.destroy()
    

            # stop after last frame
            elif loop == True:
                self.canvas.itemconfig(self.image, image=self.sequence[frame])
                self.inherit.after(speed, lambda: self.animate((frame + 1) % len(self.sequence)))

        # countdown to takePicture function
        def CameraCountdown(self):
            main.destroy()
            os.system('sleep 3 && mpg123 /home/pi/CSC132-Final/audio/camera.mp3 &')
            run_animation('CameraCountdown', 1, 1200, False, False)

        def pictureTime(self):
            tryUnlock = takePicture()
            main.destroy()
            # Unlock Lock
            if tryUnlock == True:
                os.system('mpg123 /home/pi/CSC132-Final/audio/accessGranted.mp3 &')
                unlock = unlockDoor()
                run_animation('auth', 1, 3000, False, True)
                lock = lockDoor()
                run_animation('Default_Screen', 0, 50, True, False)
            else:
                os.system('mpg123 /home/pi/CSC132-Final/audio/accessDenied.mp3 &')
                run_animation('notAuth', 1, 3000, False, True)
                numPad.launch()
                unlock = unlockDoor()
                run_animation('auth', 1, 3000, False, True)
                lock = lockDoor()
                run_animation('Default_Screen', 0, 50, True, False)


    ### Create Window and run current animation ###
    main = tkinter.Tk()    
    animate = Animation(main)

    # detect touch and shift GUI image accordingly
    guiFlow = {0:Animation.CameraCountdown, 1:Animation.pictureTime}
    for key, value in guiFlow.items():
        if key == position:
            main.bind("<Button-1>", value)

    # full screen
    main.attributes('-fullscreen', True)
    main.mainloop()

run_animation('Default_Screen', 0, 50, True, False)
