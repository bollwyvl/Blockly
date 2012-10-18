import sh

def browserify():
    possible = [
        fname.strip()
        for fname in sh.find(".", "-name", "*.js")
        if not fname.strip().endswith("min.js")
            and fname.strip() != "./blockly.js"
    ]
        
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