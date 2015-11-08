# import urllib2
import os
from urllib2 import urlopen, URLError, HTTPError

indexlistBase = "https://raw.githubusercontent.com/sanskrit-coders/"
listOfIndexes = [
    "stardict-sanskrit/master/sa-head/tars/tars.MD",
    # "/stardict-sanskrit/master/en-head/tars/tars.MD",
    # "/stardict-kannada/master/en-head/tars/tars.MD",
    # "/stardict-kannada/master/kn-head/tars/tars.MD",
    # "/stardict-pali/master/en-head/tars/tars.MD",
    # "/stardict-hindi/master/dev-head/tars/tars.MD",
]


# download the url into dir
# if dir does not exist create it
def dlfile(url, dir):
    import pdb; pdb.set_trace()
    # Open the url
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        f = urlopen(url)
        print "downloading " + url
        localpath = dir + "/" + os.path.basename(url)
        print localpath
        # Open our local file for writing
        with open(localpath, "wb") as local_file:
            local_file.write(f.read())

    # handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


def downloadDictionaries(base, listOfIndexes, tmpDirectory, downloadDir):
    for indexUrl in listOfIndexes:
        fullIndexPath = base + indexUrl
        # download this index
        response = urlopen(fullIndexPath)
        for line in response:
            line = line.rstrip()
            linelen = len(line)
            dictURL = line[1:linelen-1]
            # dictURL is a URl to a .tar.gz file
            # this needs to be extracted in a subdirectory of downloadsDir
            print dictURL

if __name__ == '__main__':
    # downloadDictionaries(indexlistBase, listOfIndexes,
    #                     "./sdcard/Download/dicttars")
    dlfile('http://www.kathamrita.org/wp-content/uploads/2013/12/divinity.jpg', 'files/files')
