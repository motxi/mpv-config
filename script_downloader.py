import re
import os
import requests
from pathlib import Path
from typing import List

def download_scripts(urls: List[str]) -> None:
    directory = Path(__file__).parent.absolute() / "scripts"

    if not os.path.exists(directory):
        os.mkdir(directory)

    for url in urls:
        filename = re.match(r".+\/(.+\.lua)", url)[1]
        save = directory / filename
        request = requests.get(url)

        with open(save, "w+", encoding="utf-8", newline="") as file:
            print(f"Downloading script {filename}")
            file.write(request.text)

if __name__ == "__main__":
    urls = [
        "https://raw.githubusercontent.com/mpv-player/mpv/master/TOOLS/lua/autoload.lua",
        "https://raw.githubusercontent.com/detuur/mpv-scripts/master/boss-key.lua",
        "https://raw.githubusercontent.com/Arieleg/mpv-copyTime/master/copyTime.lua",
        "https://github.com/ekisu/mpv-webm/releases/download/latest/webm.lua"
    ]

    download_scripts(urls)
