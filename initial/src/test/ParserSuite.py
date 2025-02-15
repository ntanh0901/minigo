import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_valid_vardecl_1(self):
        input = "var c int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_valid_vardecl_2(self):
        input = "var d int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_valid_vardecl_3(self):
        input = "var e int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_valid_vardecl_4(self):
        input = "var f int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_valid_vardecl_5(self):
        input = "var g int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_valid_vardecl_6(self):
        input = "var h int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_valid_vardecl_7(self):
        input = "var i int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_valid_vardecl_8(self):
        input = "var j int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_valid_vardecl_9(self):
        input = "var k int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_valid_vardecl_10(self):
        input = "var l int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_valid_vardecl_11(self):
        input = "var m int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_valid_vardecl_12(self):
        input = "var n int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_valid_vardecl_13(self):
        input = "var o int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_valid_vardecl_14(self):
        input = "var p int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_valid_vardecl_15(self):
        input = "var q int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_valid_vardecl_16(self):
        input = "var r int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_valid_vardecl_17(self):
        input = "var s int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_valid_vardecl_18(self):
        input = "var t int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_valid_vardecl_19(self):
        input = "var u int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_valid_vardecl_20(self):
        input = "var v int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_valid_vardecl_21(self):
        input = "var w int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_valid_vardecl_22(self):
        input = "var x int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_valid_vardecl_23(self):
        input = "var y int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_valid_vardecl_24(self):
        input = "var z int ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_valid_funcdecl_1(self):
        input = "func a () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_valid_funcdecl_2(self):
        input = "func b () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_valid_funcdecl_3(self):
        input = "func c () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_valid_funcdecl_4(self):
        input = "func d () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_valid_funcdecl_5(self):
        input = "func e () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_valid_funcdecl_6(self):
        input = "func f () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_valid_funcdecl_7(self):
        input = "func g () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_valid_funcdecl_8(self):
        input = "func h () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_valid_funcdecl_9(self):
        input = "func i () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_valid_funcdecl_10(self):
        input = "func j () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_valid_funcdecl_11(self):
        input = "func k () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_valid_funcdecl_12(self):
        input = "func l () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_valid_funcdecl_13(self):
        input = "func m () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_valid_funcdecl_14(self):
        input = "func n () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_valid_funcdecl_15(self):
        input = "func o () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_valid_funcdecl_16(self):
        input = "func p () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_valid_funcdecl_17(self):
        input = "func q () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_valid_funcdecl_18(self):
        input = "func r () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_valid_funcdecl_19(self):
        input = "func s () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_valid_funcdecl_20(self):
        input = "func t () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_valid_funcdecl_21(self):
        input = "func u () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_valid_funcdecl_22(self):
        input = "func v () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_valid_funcdecl_23(self):
        input = "func w () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_valid_funcdecl_24(self):
        input = "func x () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_error_6_new(self):
        input = "var a int"
        expect = "Error on line 1 col 9: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_error_7_new(self):
        input = "var a int ; extra"
        expect = "Error on line 1 col 11: extra"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_error_8_new(self):
        input = "int a ;"
        expect = "Error on line 1 col 1: int"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_error_9_new(self):
        input = "var a ;"
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_error_10_new(self):
        input = "func main ) { } ;"
        expect = "Error on line 1 col 10: )"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_error_11_new(self):
        input = "func main ( { } ;"
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_error_12_new(self):
        input = "func main() } ;"
        expect = "Error on line 1 col 10: }"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_error_13_new(self):
        input = "func main() { ;"
        expect = "Error on line 1 col 12: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_error_14_new(self):
        input = "func main() { }"
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_error_15_new(self):
        input = "main() { } ;"
        expect = "Error on line 1 col 1: main"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_error_16_new(self):
        input = "func main() { } extra"
        expect = "Error on line 1 col 16: extra"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_error_17_new(self):
        input = "varr a int ;"
        expect = "Error on line 1 col 1: varr"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_error_18_new(self):
        input = "func 123() { } ;"
        expect = "Error on line 1 col 6: 1"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_error_19_new(self):
        input = "var A int ;"
        expect = "Error on line 1 col 5: A"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_error_20_new(self):
        input = "junk var a int ;"
        expect = "Error on line 1 col 1: j"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_error_21_new(self):
        input = "funcmain() { } ;"
        expect = "Error on line 1 col 1: funcmain"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_error_22_new(self):
        input = "func main( { } ;"
        expect = "Error on line 1 col 10: ("
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_error_23_new(self):
        input = "var a int ;;"
        expect = "Error on line 1 col 10: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_error_24_new(self):
        input = "func main() {{ } ;"
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_error_25_new(self):
        input = "var a int lol"
        expect = "Error on line 1 col 11: lol"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_valid_funcdecl_25(self):
        input = "func y () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_valid_funcdecl_26(self):
        input = "func z () { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_valid_funcdecl_27(self):
        input = "func main() { var a int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_valid_funcdecl_28(self):
        input = "func main() { func foo() { } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_valid_funcdecl_29(self):
        input = "func main() { var a int ; func foo() { } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_valid_funcdecl_30(self):
        input = "func main() { var a int ; var b int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_valid_funcdecl_31(self):
        input = "func main() { var a int ; var b int ; func foo() { } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_valid_funcdecl_32(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_valid_funcdecl_33(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_valid_funcdecl_34(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_valid_funcdecl_35(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_valid_funcdecl_36(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_valid_funcdecl_37(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_valid_funcdecl_38(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_valid_funcdecl_39(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_valid_funcdecl_40(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_valid_funcdecl_41(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_valid_funcdecl_42(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_valid_funcdecl_43(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; func corge() { } ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_valid_funcdecl_44(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; func corge() { var k int ; } ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_valid_funcdecl_45(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; func corge() { var k int ; var l int ; } ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_valid_funcdecl_46(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; func corge() { var k int ; var l int ; func grault() { } ; } ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_valid_funcdecl_47(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; func corge() { var k int ; var l int ; func grault() { var m int ; } ; } ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_valid_funcdecl_48(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; func corge() { var k int ; var l int ; func grault() { var m int ; var n int ; } ; } ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_valid_funcdecl_49(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; func corge() { var k int ; var l int ; func grault() { var m int ; var n int ; func garply() { } ; } ; } ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_valid_funcdecl_50(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; func corge() { var k int ; var l int ; func grault() { var m int ; var n int ; func garply() { var o int ; } ; } ; } ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_valid_funcdecl_51(self):
        input = "func main() { var a int ; var b int ; func foo() { var c int ; var d int ; func bar() { var e int ; var f int ; func baz() { var g int ; var h int ; func qux() { var i int ; var j int ; func corge() { var k int ; var l int ; func grault() { var m int ; var n int ; func garply() { var o int ; var p int ; } ; } ; } ; } ; } ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test_valid_funcdecl_52(self):
        input = "func test52() { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))

    def test_valid_funcdecl_53(self):
        input = "func test53() { var alpha int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 302))

    def test_valid_funcdecl_54(self):
        input = "func test54() { func nested15() { } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 303))

    def test_valid_funcdecl_55(self):
        input = "func test55() { var a int ; var b int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 304))

    def test_valid_funcdecl_56(self):
        input = "func test56() { func foo() { var x int ; } ; var y int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 305))

    def test_valid_funcdecl_57(self):
        input = "func test57() { var a int ; func bar() { var b int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 306))

    def test_valid_funcdecl_58(self):
        input = "func test58() { func bar() { func baz() { } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 307))

    def test_valid_funcdecl_59(self):
        input = "func test59() { var c int ; func bar() { func baz() { } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 308))

    def test_valid_funcdecl_60(self):
        input = "func test60() { var c int ; var d int ; var e int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 309))

    def test_valid_funcdecl_61(self):
        input = "func test61() { func foo() { var i int ; var j int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 310))

    def test_valid_funcdecl_62(self):
        input = "func test62() { var a int ; var b int ; func foo() { var c int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 311))

    def test_valid_funcdecl_63(self):
        input = "func test63() { var b int ; func foo() { func bar() { var c int ; } ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 312))

    def test_valid_funcdecl_64(self):
        input = "func test64() { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 313))

    def test_valid_funcdecl_65(self):
        input = "func test65() { var x int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 314))

    def test_valid_funcdecl_66(self):
        input = "func test66() { var longVarName int ; var shortVarName int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 315))

    def test_valid_funcdecl_67(self):
        input = "func test67() { func inFunc() { var subVar int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 316))

    def test_valid_funcdecl_68(self):
        input = "func test68() { var a int ; var b int ; var c int ; func nestedFunc() { } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 317))

    def test_valid_funcdecl_69(self):
        input = "func test69() { func alpha() { var a int ; } ; func beta() { var b int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 318))

    def test_valid_funcdecl_70(self):
        input = "func test70() { var a int ; var b int ; func alpha() { var c int ; } ; func beta() {} ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 319))

    def test_valid_funcdecl_71(self):
        input = "func test71() { var a int ; func alpha() { var c int ; } ; var b int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 320))

    def test_valid_funcdecl_72(self):
        input = "func test72() { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 321))

    def test_valid_funcdecl_73(self):
        input = "func test73() { var a int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 322))

    def test_valid_funcdecl_74(self):
        input = "func test74() { var x int ; var y int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 323))

    def test_valid_funcdecl_75(self):
        input = "func test75() { func foo() {} ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 324))

    def test_valid_funcdecl_76(self):
        input = "func test76() { var x int ; func foo() { var y int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 325))

    def test_valid_funcdecl_77(self):
        input = "func test77() { func foo() { func bar() {} ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 326))

    def test_valid_funcdecl_78(self):
        input = "func test78() { var x int ; var y int ; var z int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 327))

    def test_valid_funcdecl_79(self):
        input = "func test79() { var a int ; func foo() { var b int ; } ; var c int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 328))

    def test_valid_funcdecl_80(self):
        input = "func test80() { func foo() { var x int ; var y int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 329))

    def test_valid_funcdecl_81(self):
        input = "func test81() { var a int ; func nested() { var b int ; func deeper() {} ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 330))

    def test_valid_funcdecl_82(self):
        input = "func test82() { var alpha int ; var beta int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 331))

    def test_valid_funcdecl_83(self):
        input = "func test83() { func alpha() { } ; func beta() { } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 332))

    def test_valid_funcdecl_84(self):
        input = "func test84() { var a int ; func alpha() { func gamma() {} ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 333))

    def test_valid_funcdecl_85(self):
        input = "func test85() { func alpha() { var x int ; var y int ; } ; var z int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 334))

    def test_valid_funcdecl_86(self):
        input = "func test86() { var a int ; var b int ; var c int ; var d int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 335))

    def test_valid_funcdecl_87(self):
        input = "func test87() { var a int ; func alpha() { } ; func beta() { var b int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 336))

    def test_valid_funcdecl_88(self):
        input = "func test88() { func alpha() {} ; func beta() {} ; func gamma() {} ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 337))

    def test_valid_funcdecl_89(self):
        input = "func test89() { var a int ; func alpha() { var b int ; func beta() {} ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 338))

    def test_valid_funcdecl_90(self):
        input = "func test90() { /* nested function calls for test */ func alpha() {} ; var x int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 339))

    def test_valid_funcdecl_91(self):
        input = "func test91() { var a int ; var b int ; func alpha() { var c int ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 340))

    def test_valid_funcdecl_92(self):
        input = "func test92() { } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 341))

    def test_valid_funcdecl_93(self):
        input = "func test93(){var a int ;} ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 342))

    def test_valid_funcdecl_94(self):
        input = "func test94() { var a int ; func nested() { } ; var b int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 343))

    def test_valid_funcdecl_95(self):
        input = "func test95() { var a int ; /* comment */ } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 344))

    def test_valid_funcdecl_96(self):
        input = "func test96() { func nested() {} ; /* another comment */ var b int ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 345))

    def test_valid_funcdecl_97(self):
        input = "func test97() { var a int ; func nested1() { func nested2() {} ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 346))

    def test_valid_funcdecl_98(self):
        input = "func test98() { var a int ; var b int ; func nested() { var c int ; func deeper() {} ; } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 347))

    def test_valid_funcdecl_99(self):
        input = "func test99(){};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 348))

    def test_valid_funcdecl_100(self):
        input = "func test100() { var alpha int ; var beta int ; func gamma() { } ; } ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 349))