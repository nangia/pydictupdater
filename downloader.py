import os
from urllib2 import urlopen, URLError, HTTPError
import tarfile
import platform

indexlistBase = "https://raw.githubusercontent.com/sanskrit-coders/"
listOfIndexes = [
    "stardict-sanskrit/master/sa-head/tars/tars.MD",
    "stardict-sanskrit/master/en-head/tars/tars.MD",
    "stardict-kannada/master/en-head/tars/tars.MD",
    "stardict-kannada/master/kn-head/tars/tars.MD",
    "stardict-pali/master/en-head/tars/tars.MD",
    "stardict-hindi/master/dev-head/tars/tars.MD",
]


# create the directory if it does not exist already
def createDirectory(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


# download the url into dir
# if dir does not exist create it
def dlfile(url, dir, forcedownload=True):
    createDirectory(dir)
    # Open the url
    try:
        f = urlopen(url)
        localpath = dir + "/" + os.path.basename(url)
        # Open our local file for writing
        if not forcedownload:
            if os.path.isfile(localpath):  # check if this file exists
                print "skipped %s as it already exists" % localpath
                return
        with open(localpath, "wb") as local_file:
            local_file.write(f.read())

    # handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


# take an indexURL and return list of .tar.gz listed in it
def getListOfDownloadFiles(indexURL, verbose=False):
    returnlist = []
    if verbose:
        print "Processing index %s" % indexURL
    # download this index and go through it line by line
    response = urlopen(indexURL)
    for line in response:
        line = line.rstrip()  # remove line marker
        linelen = len(line)
        dictURL = line[1:linelen-1]  # strip away '<' & '>' at begining & end
        # dictURL is a URl to a .tar.gz file
        returnlist.append(dictURL)
    return returnlist


def downloadAndExtractDictionary(dictURL, tmpDirectory, downloadDir,
                                 forcedownload=False):
    dictfilename = os.path.basename(dictURL)
    print "downloading file=%s, to dir=%s" % (
        dictfilename,
        tmpDirectory)
    dlfile(dictURL, tmpDirectory, forcedownload)
    assert(dictfilename[-7:] == ".tar.gz")
    t = tarfile.open(tmpDirectory + "/" + dictfilename, 'r')
    thedictfilenamelen = len(dictfilename)
    subDirnameToExtract = dictfilename[:thedictfilenamelen - 7]
    fullpathofsubdir = downloadDir + subDirnameToExtract
    print "extract to %s" % fullpathofsubdir
    t.extractall(fullpathofsubdir)


def downloadDictionaries(base, listOfIndexes, tgzDownloadDirectory,
                         dictExtractDir,
                         maxcount=1, forcedownload=False, verbose=False):
    count = 0
    for indexUrl in listOfIndexes:
        fullIndexPath = base + indexUrl
        # download this index
        if verbose:
            print "============================================"
            print "Processing index %s" % fullIndexPath
        dictlist = getListOfDownloadFiles(fullIndexPath, verbose=True)
        for adict in dictlist:
            downloadAndExtractDictionary(adict, tgzDownloadDirectory,
                                         dictExtractDir, forcedownload)
            count += 1
            if count == -1:
                continue  # no limit to download
            if count == maxcount:
                return
        if verbose:
            print "============================================"


def getMasterListToDownload(base, listOfIndexes, verbose=False):
    masterlist = []
    for indexUrl in listOfIndexes:
        fullIndexPath = base + indexUrl
        # download this index
        if verbose:
            print "============================================"
            print "Processing index %s" % fullIndexPath
        dictlist = getListOfDownloadFiles(fullIndexPath, verbose=True)
        masterlist.extend(dictlist)
        return masterlist


if __name__ == '__main__':
    onCompu = True
    tmpDir = "/sdcard/Download/dicttars"
    dictDir = "/sdcard/dictdata/"
    onMac = (platform.system() == 'Darwin')
    if onMac:
        tmpDir = "." + tmpDir
        dictDir = "." + dictDir
    downloadDictionaries(indexlistBase, listOfIndexes,
                         tmpDir, dictDir, maxcount=-1, forcedownload=False,
                         verbose=True)
