import sys
import os

from subprocess import Popen, PIPE, call

def check_command( command ):
    result = True
    try:
        p = Popen( [ command ], stdout = PIPE, stderr = PIPE)
        out, err = p.communicate()
    except:
        result = False
    finally:
        pass

    return result

class SWFExtractor:
    def __init__(self):
        self.tool_name='swfextract.exe'
        self.is_available=check_command(self.tool_name)

    def is_extractor_ready(self):
        if not self.is_available:
            print( self.tool_name + " is not acessible")
            return False
        return True

    def get_ids(self, ids):
        return []

    def get_images( self, package):
        command = [ self.tool_name, package]

        p = Popen(command, stdout = PIPE, stderr = PIPE)
        out, err = p.communicate()

        out_strings = out.decode("utf-8").splitlines()

        jpgs = []
        pngs = []
        err = None

        for str in out_strings:
            if str.startswith('[-j]'):
                jpgs = get_ids(str)
            elif str.startswith('[-p]'):
                pngs = get_ids(str)

        if (len(jpgs) == 0) and ( len(pngs) == 0):
            err = 'There are no images in SWF file'

        return jpgs, pngs, err

    def extract_images(self, package, out_path=None):
        if not self.is_available:
            return False

        if not os.path.exists(package):
            print('SWF file not found: ' + package)
            return False

        if out_path == None:
            out_path = os.getcwd()

        print( 'Out set to: ' + out_path)

        jpg_list, png_list, err = self.get_images(package)
        if err:
            print( err )
            return False

        return True

    def

def extract_images_from_swf(package, out_path=None):
    extractor = SWFExtractor()

    if not extractor.is_extractor_ready():
        return False

    if not extractor.extract_images(package, out_path):
        print( 'Failed to extract images')
        return False

    return True

def print_usage():
    print("Usage:")
    print( __file__ + " swf_file [output dir]")

if __name__ == '__main__':
    args = len(sys.argv)
    if (args < 2) or (args > 3):
        print_usage()
    else:
        if args == 2:
            extract_images_from_swf( sys.argv[1] )
        else:
            extract_images_from_swf( sys.argv[1], sys.args[2] )