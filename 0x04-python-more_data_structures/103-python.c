#include <Python.h>
#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_bytes - function that gives data of the Py Bytes Objects.
 *
 * @p: the Py Objects.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &string, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
		while (i < size + 1 && i < 10)
		{
			printf(" %02hhx", string[i]);
			i++;
		}
		printf("\n");
	}
}

/**
 * print_python_list - funtions that gives data of the Py List Object.
 *
 * @p: the PyObject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int g = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (g < size)
		{
			item = PyList_GET_ITEM(p, g);
			printf("Element %d: %s\n", g, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			g++;
		}
	}
}
