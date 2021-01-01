#!/usr/bin/env python3

"""
The Mutable component to module DataConda (http://easy-breezy.xyz/DataConda / https://github.com/ploppy-pigeon/DataConda) by Vinayak Vikram
"""

class Mutable():
    """
    Easy parsing and converting
    """
    def __init__(self, data):
        global tt
        tt = data
    class Parsable():
        """
        Easily parse things
        """
        def __init__(self):
            self.text = tt
        def quoteparse(self, splitter:str=" + ", quotechars:list=["'", '"'], vs:dict={}, sp:list=[' + ', '"', "'"], esc:tuple=('\\', '\\'), escmode:bool=True):
            """
            Drop the boring Regexing, just use quoteparse to parse your text
            splitter is what you use to add parts together (default to ' + ')
            quotechars is a list of chracters used as quotation marks
            vs is a dictionary of variables, each key is the variable name, each value is the variable value
            sp is a list of special characters
            esc is a tuple of 2 characters, one is the starting escape character, one is the ending escape character
            escmode is the escape mode. If escmode is True, only a starting escape character is used. If escmode is False, a starting and a ending escape character are used
            """
            text = self.text.split(splitter)
            self.vrs = vs
            output = []
            qchars = []
            for q in quotechars:
                qchars.append(q[0])
            for t in range(len(text)):
                txt = text[t]
                if txt[0] in qchars and txt[-1] in qchars:
                    output.append(txt[1:-1])
                elif txt[0] == esc[0][0] and txt[-1] == esc[1][0] and escmode == False:
                    output.append(sp[int(txt[1:-1])])
                elif txt[0] == esc[0][0] and escmode == True:
                    output.append(sp[int(txt[1:])])
                else:
                    name = txt
                    try:
                        output.append(str(self.vrs[name]))
                    except KeyError:
                        raise NameError("Variable " + txt + " does not exist")
            penultimate = tuple(output)
            end = "".join(penultimate)
            return end
        def cmdparse(self, argchars:tuple=("(", ")"), argsep:str=","):
            cmd = self.text[:self.text.find(argchars[0])]
            args = self.text[self.text.find(argchars[0]) + len(argchars[0]):len(self.text) - len(argchars[1])]
            return cmd, args.split(argsep)
    class Convertible():
        def __init__(self):
            self.text = tt
        def to_table(self):
            """
            Convert a dictionary to a table
            """
            try:
                table = self.text
                tabl = []
                hi = 0
                for h1, h2 in table.items():
                    if len(h1) > hi:
                        hi = len(h1)
                    if len(h2) > hi:
                        hi = len(h2)
                tabl.append("-" * ((hi * 2) + 5))
                for c1, c2 in table.items():
                    v1 = " " * (hi - len(c1))
                    v2 = " " * (hi - len(c2))
                    tabl.append("|" + c1 + v1 + " | " + c2 + v2 + "|")
                    tabl.append("-" * ((hi * 2) + 5))
                tabl = tuple(tabl)
                tabl = "\n".join(tabl)
                return tabl
            except AttributeError:
                raise TypeError("Only dictionaries can be expressed as tables, not " + str(type(table))[8:-2] + "s")  
