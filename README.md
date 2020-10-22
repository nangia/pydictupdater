An alternative for [Sanskrit Dictionary Updater](https://play.google.com/store/apps/details?id=sanskritcode.sanskritdictionaryupdater)
==================

[StarDict](http://www.stardict.org) is a cross-platform and international dictionary software. Using StartDict or other apps that work with the StarDict dictionary format, one could use this for a dictionary of various languages.

[Vishvas Vasuki](https://github.com/vvasuki) and [others](https://github.com/sanskrit-coders) have compiled a nice set of dictionaries for [Indic Languages](https://github.com/indic-dict). Thus, one could use a StarDict compatible app like [EBDic](https://apkpure.com/ebdic/com.twn.ebdic), [GoldenDict](https://play.google.com/store/apps/details?id=mobi.goldendict.android), or [ColorDict](https://play.google.com/store/apps/details?id=com.socialnmobile.colordict) which can be used for these dictionaries. The process would be to install GoldenDict and then install and run [Sanskrit Dictionary Updater](https://play.google.com/store/apps/details?id=sanskritcode.sanskritdictionaryupdater) (again written by Vishvas) and then rescan dictionaries from within GoldenDict App.

However, I have had problems running Sanskrit Dictionary Updater on my phone recently. Hence, I just wrote this as an alternative way to download these dictionaries to your Desktop computer or to Android for myself. Note you may not need this and Sanskrit Dictionary Updater might just work for you very well. But, I needed this for myself so wrote this. 

Update (2020/10/22): Due to issues with running [Sanskrit Dictionary Updater](https://play.google.com/store/apps/details?id=sanskritcode.sanskritdictionaryupdater) on a Moto G Stylus, this was forked from [the original](https://github.com/sanskrit-coders/pydictupdater) to python3 and used as a backup. It is not in the greatest of shape, and needs some work to be a good general tool - @kmadathil

What Platforms Will this App Run on?
====================================
This version of the software was tested on Ubuntu Linux with Python 3.7. It should run on any Linux system or MacOS with Python3. It may not run on Windows, but should run with minor edits.

Controlling the Dict Files Downloaded
==========================================

The default setting downloads Sanskrit, Pali, Hindi and Malayalam dictionaries. There are others available (Kannada, Telugu, Tamil, etc.) which can be downloaded by modifying the file directly.

Edit downloader.py and add the index files you want from [Indic Dicts](https://github.com/indic-dict). Comment out the index files that you don't want by putting a "#" on that line.

```
python
listOfIndexes = [
    "stardict-sanskrit/gh-pages/sa-head/sa-entries/tars/tars.MD",
    "stardict-sanskrit/gh-pages/sa-head/en-entries/tars/tars.MD",
    "stardict-sanskrit/gh-pages/en-head/tars/tars.MD",
    "stardict-sanskrit-vyAkaraNa/gh-pages/tars/tars.MD",
    "stardict-sanskrit-kAvya/gh-pages/tars/tars.MD",
    "stardict-hindi/gh-pages/hi-head/hi-entries/tars/tars.MD",
    "stardict-hindi/gh-pages/hi-head/en-entries/tars/tars.MD",
# Bad?
#    "stardict-hindi/gh-pages/en-head/tars/tars.MD",
    "stardict-malayalam/gh-pages/ml-head/tars/tars.MD",
    "stardict-malayalam/gh-pages/en-head/tars/tars.MD",
    "stardict-pali/gh-pages/pali-en-head/tars/tars.MD",
    "stardict-pali/gh-pages/pali-head/en-entries/tars/tars.MD",
    "stardict-pali/gh-pages/en-head/tars/tars.MD",
]
```
How to use pydictupdater
===============

Steps for downloading on Linux/Mac
---

1. You already will have a Python installed on Mac. Type `python3` on command line to check that. Type `quit()` to exit from Python.
2. Clone this repository using git or just download the file [downloader.py](https://raw.githubusercontent.com/nangia/pydictupdater/master/downloader.py). **Please remember to read the section "Controlling the Dict Files Downloaded" above.**
3. Type the following command in a new directory. `python3 downloader.py` 
4. The .tar.gz dictionary files will get downloaded to `./sdcard/Download/dicttars` and their expansions will be put in `./sdcard/Download/`.


Transferring the files to Android
------
You should have downloaded the files using the steps in previous section.

1. Install [GoldenDict](https://play.google.com/store/apps/details?id=mobi.goldendict.android) or [ColorDict](https://play.google.com/store/apps/details?id=com.socialnmobile.colordict) some other StarDict compatible dictionary App.
2. Transfer the .tar.gz files to from `./sdcard/Download/dicttars` (on Mac) to `/sdcard/Download/dicttars` on Android and all files (and subdirectories) from `./sdcard/Download` to `/sdcard/Download` on Android. You can do this via [adb](http://developer.android.com/intl/ja/tools/help/adb.html) or any other mechanism.
3. Now run GoldenDict or ColorDict and Rescan dictionaries. You should be all set now!


Transferring files to iOS  
---
You should have downloaded the dictionaries as decribed in the Mac section above. This should work (I haven't tested personally. Though a friend has used Dictionary Universal and downloaded .tar.gz files directly):

1. You should install a StarDict compatible app like [Dictionary Universal](https://itunes.apple.com/in/app/dictionary-universal/id312088272?mt=8) on your iPhone.
2. Download dictionaries on a Mac as given in above steps.
3. Copy the .tar.gz files to your iPhone using the process described [here](http://dictionary-universal.appspot.com/dictionary/en/manuals.html) via USB or WiFi.

Running directly on Android 
------
If you want to run directly on Android, use the following steps:

1. Install [QPython](https://play.google.com/store/apps/details?id=com.hipipal.qpyplus). 
2. On a computer, click on [downloader.py](https://raw.githubusercontent.com/nangia/pydictupdater/master/downloader.py) in a browser.
3. Transfer this program to `/sdcard/com.hipipal.qpyplus/scripts` on Android. [You can use pushtoandroid.sh].
4. Now run QPython and run the program. Be patient! It might take a while to download. It would be prudent to do this while you are connected to WiFi or have a fast internet connection. This will download and install the dictionaries on your Android phone.
6. Now run GoldenDict or ColorDict and Rescan dictionaries. You are all set now!


Other Platforms
---------------
I have not tested this on Windows or other platforms. But, the program should work with minor changes as long as Python 3.x is available. You might want to change the paths where .tar.gz files and their expansions are stored. 



