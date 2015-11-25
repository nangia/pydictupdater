An alternative for [Sanskrit Dictionary Updater](https://play.google.com/store/apps/details?id=sanskritcode.sanskritdictionaryupdater)
==================

[StarDict](http://www.stardict.org) is a cross-platform and international dictionary software. Using StartDict or other apps that work with the StarDict dictionary format, one could use this for a dictionary of various languages.

[Vishvas Vasuki](https://github.com/vvasuki) ([@vasukeya](https://twitter.com/vasukeya) on Twitter) and [others](https://github.com/sanskrit-coders) have compiled a nice set of dictionaries  that work with StarDict compatible apps for [Sanskrit](https://github.com/sanskrit-coders/stardict-sanskrit), [Kannada](https://github.com/sanskrit-coders/stardict-kannada), [Pali](https://github.com/sanskrit-coders/stardict-pali) and [Hindi](https://github.com/sanskrit-coders/stardict-hindi). Thus, one could use a StarDict compatible app like [GoldenDict](https://play.google.com/store/apps/details?id=mobi.goldendict.android) which can be used for these dictionaries. The process would be to install GoldenDict and then install and run [Sanskrit Dictionary Updater](https://play.google.com/store/apps/details?id=sanskritcode.sanskritdictionaryupdater) (again written by Vishvas) and then rescan dictionaries from within GoldenDict App.

However, I have had problems running Sanskrit Dictionary Updater on my phone recently. Hence, I just wrote this as an alternative way to download these dictionaries to your Desktop computer or to Android for myself. Note you may not need this and Sanskrit Dictionary Updater might just work for you very well. But, I needed this for myself so wrote this. 

What Platforms Will this App Run on?
====================================
I have tested this on a OS X Yosemite 10.10.5 and on Android 4.4. While this should work with other operating systems as well that support Python 2.7, I haven't tested it.


How to use pydictupdater
===============

If you don't want all the dictionaries, see section "What if I don't want Kannada or Pali files" first on how to customize the ```downloader.py``` program that will be used.

Running directly on Android
------
If you want to run directly on Android, use the following steps:

1. Install [QPython](https://play.google.com/store/apps/details?id=com.hipipal.qpyplus). 
2. On a computer, click on [downloader.py](https://raw.githubusercontent.com/nangia/pydictupdater/master/downloader.py) in a browser.
3. Copy paste the entire program above and paste it at [this site for generating QR code](http://qpython.com/#qrcode) after removing the existing python program there. And click on Create. This will generate a QR code image.
4. Using QPython, scan the above QR code image and run the program. Be patient! It might take a while to download. It would be prudent to do this while you are connected to WiFi or have a fast internet connection. This will download and install the dictionaries on your Android phone.
6. Now run GoldenDict and Rescan dictionaries. You are all set now!

Steps for downloading on Mac
---

1. You already will have a Python installed on Mac. Type `python` on command line to check that. Type `quit()` to exit from Python.
2. Clone this repository using git or just download the file [downloader.py](https://raw.githubusercontent.com/nangia/pydictupdater/master/downloader.py). If you don't want all the dictionaries, see the section "What if I don't want Kannada or Pali files" below.
3. Type the following command in a new directory. `python downloader.py` 
4. The .tar.gz dictionary files will get downloaded to `./sdcard/Download/dicttars` and their expansions will be put in `./sdcard/Download/`.


Transferring the files to Android
------
You should have downloaded the files using the steps in previous section.

1. Install [GoldenDict](https://play.google.com/store/apps/details?id=mobi.goldendict.android) or some other StarDict compatible dictionary App.
2. Transfer the .tar.gz files to from `./sdcard/Download/dicttars` (on Mac) to `/sdcard/Download/dicttars` on Android and all files (and subdirectories) from `./sdcard/Download` to `/sdcard/Download` on Android. You can do this via [adb](http://developer.android.com/intl/ja/tools/help/adb.html) or any other mechanism.
3. Now run GoldenDict and Rescan dictionaries. You should be all set now!


Transferring files to iOS
---
You should have downloaded the dictionaries as decribed in the Mac section above. This should work (I haven't tested personally. Though a friend has used Dictionary Universal and downloaded .tar.gz files directly):

1. You should install a StarDict compatible app like [Dictionary Universal](https://itunes.apple.com/in/app/dictionary-universal/id312088272?mt=8) on your iPhone.
2. Download dictionaries on a Mac as given in above steps.
3. Copy the .tar.gz files to your iPhone using the process described [here](http://dictionary-universal.appspot.com/dictionary/en/manuals.html) via USB or WiFi.


Other Platforms
---------------
I have not tested this on Windows or other platforms. But, the program should work as long as Python 2.x is available. You might want to change the paths where .tar.gz files and their expansions are stored. 



What if I don't want Kannada or Pali files
==========================================
Edit downloader.py and command out the index files that you don't want by putting a "#" on that line and run "downloader.py".

```python
listOfIndexes = [
    "stardict-sanskrit/master/sa-head/tars/tars.MD",
    "stardict-sanskrit/master/en-head/tars/tars.MD",
#    "stardict-kannada/master/en-head/tars/tars.MD",
#   "stardict-kannada/master/kn-head/tars/tars.MD",
#    "stardict-pali/master/en-head/tars/tars.MD",
    "stardict-hindi/master/dev-head/tars/tars.MD",
]
```