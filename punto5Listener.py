# Generated from punto5.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .punto5Parser import punto5Parser
else:
    from punto5Parser import punto5Parser

# This class defines a complete listener for a parse tree produced by punto5Parser.
class punto5Listener(ParseTreeListener):

    # Enter a parse tree produced by punto5Parser#AddSub.
    def enterAddSub(self, ctx:punto5Parser.AddSubContext):
        pass

    # Exit a parse tree produced by punto5Parser#AddSub.
    def exitAddSub(self, ctx:punto5Parser.AddSubContext):
        pass


    # Enter a parse tree produced by punto5Parser#MulDiv.
    def enterMulDiv(self, ctx:punto5Parser.MulDivContext):
        pass

    # Exit a parse tree produced by punto5Parser#MulDiv.
    def exitMulDiv(self, ctx:punto5Parser.MulDivContext):
        pass


    # Enter a parse tree produced by punto5Parser#Parens.
    def enterParens(self, ctx:punto5Parser.ParensContext):
        pass

    # Exit a parse tree produced by punto5Parser#Parens.
    def exitParens(self, ctx:punto5Parser.ParensContext):
        pass


    # Enter a parse tree produced by punto5Parser#ComplexNum.
    def enterComplexNum(self, ctx:punto5Parser.ComplexNumContext):
        pass

    # Exit a parse tree produced by punto5Parser#ComplexNum.
    def exitComplexNum(self, ctx:punto5Parser.ComplexNumContext):
        pass



del punto5Parser