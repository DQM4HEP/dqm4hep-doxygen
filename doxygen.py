"""
"""

import json
import sys
import argparse



def addPackage(data, package, version):
    if not data.has_key("packages"):
        data["packages"] = {}
    
    if not data["packages"].has_key(package):
        data["packages"][package] = {}
    
    if not data["packages"][package].has_key("versions"):
        data["packages"][package]["versions"] = []
    
    if not version in data["packages"][package]["versions"]:
        data["packages"][package]["versions"].append(version)


def checkPackageVersion(data, package, version):
    if not data.has_key("packages"):
        return False
    
    if not data["packages"].has_key(package):
        return False
    
    if not data["packages"][package].has_key("versions"):
        return False
    
    if not version in data["packages"][package]["versions"]:
        return False
    
    return True
    

if __name__ == "__main__" :
    
    parser = argparse.ArgumentParser("Doxygen meta data API:", formatter_class=argparse.RawTextHelpFormatter, 
                            add_help=True)
    
    # io options
    parser.add_argument("--input", action="store", type=type(""), default="meta.json",
                            help="The json intput file", required=True)
    parser.add_argument("--output", action="store", default="",
                            help="The json output file", required=False)
    
    # pkg config
    parser.add_argument("--add-pkg", action="store_true", default="",
                            help="Add a new software package", required=False)
    parser.add_argument("--pkg-name", action="store", default="",
                            help="The package name if the option --add-pkg is used", required=False)
    parser.add_argument("--pkg-version", action="store", default="",
                            help="The package version if the option --add-pkg is used", required=False)                       
                            
    
    parsed = parser.parse_args()
    
    data = json.load(open(parsed.input))
    
    # add a new package
    if parsed.add_pkg:
        package = parsed.pkg_name
        version = parsed.pkg_version
        
        addPackage(data, package, version)
        
    # write out the meta data
    if parsed.output:
        fout = open(parsed.output, 'w')
        fout.write(json.dumps(data, sort_keys=False, indent=2))
        fout.close()
