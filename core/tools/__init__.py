from . import tool_temp
from .timeTool import TimeTool
from .dateTool import DateTool
from .openWeatherMapTool import OpenWeatherMapTool
from .websiteOpener import WebsiteOpenerTool
from .youtubeSearchTool import YoutubeSearchTool
from .screenshotTool import ScreenshotTool
from .spotifySearchTool import SpotifySearchTool
from .spotifyPlayTool import SpotifyPlayTool
from .calendarTool import calendar_tool
from .emailTool import email_tool
from .fileOpsTool import file_ops_tool
from .systemControlTool import system_control_tool
from .clipboardTool import clipboard_tool
from .webSearchTool import web_search_tool

def get_tools():
    return [
            TimeTool(),
            DateTool(),
            OpenWeatherMapTool(),
            WebsiteOpenerTool(),
            YoutubeSearchTool(),
            ScreenshotTool(),
            SpotifySearchTool(),
            SpotifyPlayTool(),
            calendar_tool,
            email_tool,
            file_ops_tool,
            system_control_tool,
            clipboard_tool,
            web_search_tool,
        ]

def reset_all_tools():
    tool_temp.reset_all_temp()

def get_tools_used():
    return tool_temp.get_tools_used()