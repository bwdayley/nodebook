from optparse import OptionParser
import os
import shutil

def getHourAndFile(path):
    pathItems = path.split(os.sep)
    return (pathItems[3], pathItems[-1])

def addLineNos(fName, outPath):
    fIn = open(fName, 'r')
    lines = fIn.readlines()
    fIn.close()
    (hour, filename) = getHourAndFile(fName)
    if not os.path.exists(os.path.join(outPath, hour)):
        os.system("mkdir %s" % os.path.join(outPath, hour))
    outFile = os.path.join(outPath, hour, filename+'.lineno')
    fOut = open(outFile, 'w')
    padding = 1
    if len(lines) > 9:
        padding = 2
    if len(lines) > 99:
        padding = 3
    lineNo = 0
    for line in lines:
        lineNo += 1
        outStr = "%%0%dd %%s" % padding
        fOut.write(outStr % (lineNo, line))
    fOut.close()
    print "Generated %s" % outFile


skipFolders = ['node_modules']
def processDir(fPath, outPath):
    entries = os.listdir(fPath)
    for entry in entries:
        newPath = os.path.join(fPath,entry)
        if os.path.isdir(newPath) and entry not in skipFolders:
            processDir(newPath, outPath)
        elif os.path.isfile(newPath):
            ext = entry.split('.')[-1]
            if ext in ['html','js','css', 'php', 'xml', 'json']:
                addLineNos(os.path.join(fPath, entry), outPath)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="File to add line numbers to", metavar="FILE")
    parser.add_option("-p", "--path", dest="filepath", help="Path to Files to add line numbers to", metavar="PATH")
    parser.add_option("-o", "--output", dest="output", help="Path to output linenumbered files to", metavar="OUTPUT")
    (options, args) = parser.parse_args()
    fName = options.filename
    fPath = options.filepath
    outPath = options.output
    if not outPath:
        outPath = 'c:\\_node\\lineno'
    if os.path.exists(outPath):
        shutil.rmtree(outPath)
    os.makedirs(outPath)
    if fName:
        if not os.path.exists(fName):
            print "%s does not exist" % fName
        else:
            addLineNos(fName)
    else:
        if not fPath: fPath = 'c:\\_node\\code'
        if not os.path.exists(fPath):
            print "%s does not exist" % fPath
        else:
            processDir(fPath, outPath)
#             for root, dirs, files in os.walk(fPath):
#                 for file in files:
#                     ext = file.split('.')[-1]
#                     if ext in ['html','js','css', 'php', 'xml', 'json']:
#                         addLineNos(os.path.join(root, file), outPath)
    #raw_input()
