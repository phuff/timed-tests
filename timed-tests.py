#!/usr/bin/env python
import random

def renderEquationTemplate(top="\\vspace{1mm}", middle="\\hspace{3.5mm}", bottom="\\vspace{1mm}", randomizeTopAndMiddle=False):
    if randomizeTopAndMiddle and random.random() < .5:
        holder = top
        top = middle
        middle = holder
    return '''\\begin{equation*}
\\frac{
    \\begin{array}[b]{r}
      %s\\\\
      + %s
    \\end{array}
  }{
  %s
  }
\\end{equation*}
''' % (top, middle, bottom)

class Make10AddExtra:
    title = "Make 10 Add Extra"
    def generateEquation(self):
        first = random.randint(2, 9)
        print first
        if (10 - first) < first:
            second = random.randint(1, 10 - first + 1)
        else:
            second = random.randint(10 - first + 1, 9)
        return renderEquationTemplate(first, second)

class Doubles:
    title = "Doubles"
    def generateEquation(self):
        double = random.randint(1, 10)
        return renderEquationTemplate(double, double)

class DoublesPlus1:
    title = "Doubles Plus 1"
    def generateEquation(self):
        double = random.randint(1, 10)
        return renderEquationTemplate(top=double, middle=double+1, randomizeTopAndMiddle=True)

class TenFrame:
    title = "Ten Frame"
    def generateEquation(self):
        tenPiece = random.randint(1, 9)
        return renderEquationTemplate(top=tenPiece, bottom=10)

class Nines:
    title = "Nines"
    def generateEquation(self):
        ninePiece = random.randint(1, 9)
        return renderEquationTemplate(top=ninePiece, middle=9, randomizeTopAndMiddle=True)

class TestGenerator:
    def __init__(self, problemGenerator, cols=4, rows=6):
        self.problemGenerator = problemGenerator
        self.cols = 4
        self.rows = 6

    def generateTest(self):
        output = "\\begin{minipage}{.5\\linewidth}"
        output += "%s\\\\" % (self.problemGenerator.title, )

        for cols in xrange(self.cols):
            output += "\\begin{minipage}{.15\\linewidth}\n"
            for rows in xrange(self.rows):
                output += self.problemGenerator.generateEquation()
            output += "\\end{minipage}\n"
        output += "\\end{minipage}\n"
        output += "\\vspace{10mm}\n"
        return output

if __name__ == '__main__':
    outFile = open("doubles.tex", "w")
    tg1 = TestGenerator(Nines())
    tg2 = TestGenerator(Doubles())
    tg3 = TestGenerator(DoublesPlus1())
    tg4 = TestGenerator(TenFrame())
    output = '''\\documentclass{article}
    \\usepackage{fullpage}
    \\usepackage{mathtools}
    \\begin{document}
    \\pagenumbering{gobble}
    '''
    output += tg1.generateTest()
    output += tg2.generateTest()
    output += tg3.generateTest()
    output += tg4.generateTest()
    output += "\\end{document}\n"
    outFile.write(output)
    outFile.close()
    from subprocess import call
    call(["pdflatex", "doubles.tex"])
    call(["open", "doubles.pdf"])
