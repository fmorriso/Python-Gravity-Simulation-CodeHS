import pyautogui

class Settings:
    """ A central location to store settings needed throughout this program."""
    def __init__(self, pct:float =0.75):
        # calculate game size as a percentage of device screen size
        device_width, device_height = pyautogui.size()
        self.screenPct: float = pct

        # calculate scaled screen width & height rounded to a  multiple of 10
        self.__scaled_width: int = int((device_width * self.screenPct // 10) * 10)
        self.__scaled_height: int = int((device_height * self.screenPct // 10) * 10)

    @property
    def scaled_height(self) -> int:
        return self.__scaled_height

    @property
    def scaled_width(self) -> int:
        return self.__scaled_width

    def __str__(self) -> str:
        return f'width: {self.__scaled_width}, height: {self.__scaled_height}'

    def __repr__(self) -> str:
        return f'width: {self.__scaled_width}, height: {self.__scaled_height}'