import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;

public class test
{


    public static void main(String[] args) {

        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.execfile("pythonTest.py");
        PyObject str = interpreter.eval("repr(somme(4,5))");
        System.out.println(str.toString());

    
    }
}