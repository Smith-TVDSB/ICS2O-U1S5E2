import pytest
import student 



def test_jump():
    input_values=['jump']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert output[1]=='jumping'

def test_eat():
    input_values=['eat']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert output[1]=='eating'    

def test_scarps():
    input_values=['scarp']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert output[1]=='scarping'
def test_groundbreak():
    input_values=['groundbreak']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert output[1]=='groundbreaking'
