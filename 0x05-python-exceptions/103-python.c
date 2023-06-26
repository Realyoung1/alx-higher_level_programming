#include <Python.h>

#include <stdbool.h>
#include <sys/stat.h>
#include <limits.h>
#include <unistd.h>
#include <sys/types.h>
#include <string.h>
#include <stdio.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <errno.h>
#include <stdlib.h>

/**
 * print_python_float - func that gives data of the PyFloatObject.
 * @p: the PyObject
 */

void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, k = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (k < size + 1 && k < 10)
	{
		printf(" %02hhx", string[k]);
		k++;
	}
	printf("\n");
}

/**
 * print_python_list - func that gives data of the PyListObject
 * @p: the PyObject func
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int k = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (k < size)
		{
			item = PyList_GET_ITEM(p, k);
			printf("Element %d: %s\n", k, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			k++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
