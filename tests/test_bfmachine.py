from bfmachine import BFMachine
from io import StringIO

def test_helloworld():
    stdout = StringIO()
    bfm = BFMachine(stdin=None, stdout=stdout)
    code = """++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---
            .+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."""
    bfm.run(code)
    assert stdout.getvalue() == 'Hello World!\n'