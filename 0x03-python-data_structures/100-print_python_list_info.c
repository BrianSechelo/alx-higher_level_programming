#include <Python.h>
#include <object.h>
#include<listobject.h>

void print_python_list_info(PyObject *p)
	long int size = PyList_size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] size of the python list = %li\n", size);
	printf("[*] ALlocate = %li\n", obj->allocated)
	for (i =0; i < size; i++)
	printf("Element %i:%s\n", i, py_Type(obj->ob_item[i])->tp-name);

