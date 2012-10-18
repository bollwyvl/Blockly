import sh

def browserify():
    possible = sh.find(
        ".",
        "-name",
        "*.js",
        "!",
        "-name",
        "'*.min.js'",
        "!",
        "-name",
        "'blockly.js'")
        
    for fname in possible:
        js = file(fname.strip(), "r")
        old_val = js.read()
        js.close()
        js = file(fname.strip(), "w")
        js.write(
            ";(function(Blockly){\n%s\n}).call(this, Blockly);\n" % old_val)
        js.close()

if __name__ == "__main__":
    browserify()