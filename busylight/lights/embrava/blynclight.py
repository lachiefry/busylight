""" Embrava Blynclight Support
"""

from typing import Dict, Tuple

from ..hidlight import HIDLight
from ..light import LightInfo
import time

from ._blynclight import Command


class Blynclight(HIDLight):
    @staticmethod
    def supported_device_ids() -> Dict[Tuple[int, int], str]:
        return {
            (0x2C0D, 0x0001): "Blynclight",
            (0x2C0D, 0x000C): "Blynclight",
            (0x0E53, 0x2516): "Blynclight",
        }

    @staticmethod
    def vendor() -> str:
        return "Embrava"

    def __init__(
        self,
        light_info: LightInfo,
        reset: bool = True,
        exclusive: bool = True,
    ) -> None:

        self.command = Command()

        super().__init__(light_info, reset=reset, exclusive=exclusive)

    def on(self, color: Tuple[int, int, int]) -> None:

        with self.batch_update():
            self.command.off = 0
            self.color = color

    def play_sound(self):
        with self.batch_update():
            self.music = 1
            self.volume = 20
            self.mute = 0
            self.repeat = 0
            self.play = 1
        time.sleep(5)
        with self.batch_update():
            self.music = 0
            self.volume = 0
            self.mute = 0
            self.repeat = 0
            self.play = 0
        

    

    @property
    def red(self) -> int:
        return self.command.red

    @red.setter
    def red(self, new_value: int) -> None:
        self.command.red = new_value

    @property
    def green(self) -> int:
        return self.command.green

    @green.setter
    def green(self, new_value: int) -> None:
        self.command.green = new_value

    @property
    def blue(self) -> int:
        return self.command.blue

    @blue.setter
    def blue(self, new_value: int) -> None:
        self.command.blue = new_value

    @property
    def play(self) -> bytes:
        return self.command.play
    
    @play.setter
    def play(self, new_value: int) -> None:
        self.command.play = new_value

    @property
    def mute(self) -> bytes:
        return self.command.mute
        
    @mute.setter
    def mute(self, new_value: int) -> None:
        self.command.mute = new_value
    
    @property
    def volume(self) -> bytes:
        return self.command.volume
        
    @volume.setter
    def volume(self, new_value: int) -> None:
        self.command.volume = new_value
    
    @property
    def music(self) -> bytes:
        return self.command.music
    
    @music.setter
    def music(self, new_value: int) -> None:
        self.command.music = new_value
        
    @property
    def repeat(self) -> bytes:
        return self.command.repeat
    
    @repeat.setter
    def repeat(self, new_value: int) -> None:
        self.command.repeat = new_value

    def __bytes__(self) -> bytes:
        return self.command.bytes

    def reset(self) -> None:
        with self.batch_update():
            self.command.reset()
    
    @property          
    def play_sound(self): 
        return self.command.music
