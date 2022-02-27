import pytest
import student 

def test_default(capsys):
    input_values=['18.314159f']
    output=[]
    
    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input

    student.main()
    out,err = capsys.readouterr()
    assert '2.6163084285714' in out and '18.314159'in out
    
    
def test_simple(capsys):
    input_values=['7.7f']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()


    out,err = capsys.readouterr()
    assert '1.1' in out and '7.7' in out

def test_simple_two(capsys):
    input_values=['14.7f']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()

    out,err = capsys.readouterr()
    assert '2.1' in out and '14.7' in out

    
def test_simple_three(capsys):
    input_values=['21.14f']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()

    out,err = capsys.readouterr()
    assert '3.02' in out and '21.14' in out
