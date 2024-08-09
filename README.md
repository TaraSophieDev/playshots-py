# Playshots-Py

## Description
* This is a little script for organizing switch screenshots and videos.
* This tool will copy all the files to the coresponding folder that is named after the game id that is provided in these files. (For files without game id, it will be put into the "Unknown" folder.)
* This tool also creates a JSON file per media file, that is stored in the same place the copied media file is stored in.
    * The JSON will look like this 
        ```json
        {
        "id": "4CE9651EE88A979D41F24CE8D6EA1C23",
        "fileName": "2023083120272300-4CE9651EE88A979D41F24CE8D6EA1C23",
        "type": "image",
        "game": "Splatoon 3",
        "importDate": 1723204258.1327553,
        "takenDate": 1693506443.0
        }
        ```
    * Both dates are in Unix Time
* If a json is provided that has the key "[gameID]" and the value "GameName", then the tool will use this name instead of "Null".
    * The JSON should look like this
        ```json
        {
        "2B6F48984E2A6B29FFCDA3BA60F8E2F3": "Apex Legends",
        "4CE9651EE88A979D41F24CE8D6EA1C23": "Splatoon 3"
        }
        ```

## Usage
- You need python3 to be installed, I developed this on Pythno 3.12, but it should work with older versions of Python 3.
- To run the tool you have to use the terminal/command line
- To start Playshots you need to run the following command: ``python3 playshots.py``
1. The tool will ask for a path to the folder that contains the media files.
2. It will then ask if you want to use the json file that contains the game names. This is not needed to run this tool.

## Special Thanks

* **LauraWebDev** for being my mental support.

## Donations

If you'd like to donate to me, you can do this by going to my [Ko-fi](https://ko-fi.com/tarasophiedev) or buy/pay what you want my games on [Itch.io](https://tarasophiedev.itch.io/)

## License

This project is licensed under the MIT License, For more information, check out the included [LICENSE](LICENSE) file.