import sys
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

    def extract_images(self, package, out_path=None):
        if not is_available:
            return False

def extract_images(package, out_path=None):
    extractor = SWFExtractor()

    if not extractor.is_extractor_ready():
        return False


def print_usage():
    print("Usage:")
    print( __file__ + " swf_file [output dir]")

if __name__ == '__main__':
    args = len(sys.argv)
    if (args < 2) or (args > 3):
        print_usage()
    else:
        if args == 2:
            extract_images( sys.argv[1] )
        else:
            extract_images( sys.argv[1], sys.args[2] )