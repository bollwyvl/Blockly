#!/usr/bin/env python
"""
Utility script to find non-strict, un-functioned js files
"""
import sh

def browserify():
    ignore = [
        "./blockly.js",
        "./demos/blockly_compressed.js",
        "./demos/blockly_uncompressed.js",
    ]
    possible = [
        fname.strip()
        for fname in sh.find(".", "-name", "*.js")
        if not fname.strip().endswith("min.js")
            and fname.strip() not in ignore
    ]
        
    for fname in possible:
        js = file(fname.strip(), "r")
        old_val = js.read()
        js.close()
        
        # have we already fixed this one?
        if old_val.startswith(";function("):
            continue
        
        js = file(fname.strip(), "w")
        # this is a pretty big assumption, but appears to be holding
        js.write(
            ";(function(Blockly){\n%s\n}).call(this, Blockly);\n" % old_val)
        js.close()

if __name__ == "__main__":
    browserify()
