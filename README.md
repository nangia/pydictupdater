An alternative for [Sanskrit Dictionary Updater](https://play.google.com/store/apps/details?id=sanskritcode.sanskritdictionaryupdater)
==================

[StarDict](http://www.stardict.org) is a cross-platform and international dictionary software. Using StartDict or other apps that work with the StarDict dictionary format, one could use this for a dictionary of various languages.

[Vishvas Vasuki](https://github.com/vvasuki) ([@vasukeya](https://twitter.com/vasukeya) on Twitter) and [others](https://github.com/sanskrit-coders) have compiled a nice set of dictionaries  that work with StarDict compatible apps for [Sanskrit](https://github.com/sanskrit-coders/stardict-sanskrit), [Kannada](https://github.com/sanskrit-coders/stardict-kannada), [Pali](https://github.com/sanskrit-coders/stardict-pali) and [Hindi](https://github.com/sanskrit-coders/stardict-hindi). Thus, one could use a StarDict compatible app like [GoldenDict](https://play.google.com/store/apps/details?id=mobi.goldendict.android) which can be used for these dictionaries. The process would be to install GoldenDict and then install and run [Sanskrit Dictionary Updater](https://play.google.com/store/apps/details?id=sanskritcode.sanskritdictionaryupdater) (again written by Vishvas) and then rescan dictionaries from within GoldenDict App.

However, I have had problems running Sanskrit Dictionary Updater on my phone. Hence, this is a alternative way to download these dictionaries to your Desktop computer or to Android. 

What Platforms Will this App Run on?
====================================
I have tested this on a OS X Yosemite 10.10.5 and on Android 4.4. While this should work with other operating systems as well that support Python 2.7, I haven't tested it.

How to use this
===============

- Make sure you have Python 2.7 available on your computer. You can install from [https://www.python.org](https://www.python.org). If you want to run on Android, you can use [QPython](http://qpython.com). 

- Clone this repository using git or just download the file [downloader.py](https://raw.githubusercontent.com/nangia/pydictupdater/master/downloader.py). If you don't want all the dictionaries, see the section "What if I don't want Kannada or Pali files" below.

- If you want to run downloader.py on Android you have to transfer downloader.py to your Android. You can use the filepushtoandroid.sh to transfer it via adb. Make sure you fix the path to adb.

- Run "downloader.py". On Android, the .tar.gz dictionary files will get downloaded to /sdcard/Download/dicttars and their expansions will be put in /sdcard/Download/. If you ran this on a Mac, you would get .tar.gz files in ./sdcard/Donwload/dicttars. 

- If you are doing this on Android, you are done, just run GoldenDict and Rescan dictionaries. If you are on Desktop, transfer the files to /sdcard/Download/dicttars and then run Rescan dictionaries from within GoldenDict.


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