#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - printd python list info
 *
 * @p: pyobject
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
	const char *itemType;
	Py_ssize_t size;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[*] Python object is not a list\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		itemType = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, itemType);
	}
}

/**
 * print_python_bytes - printd python bytes info
 *
 * @p: oyobject
 *
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	PyObject *item;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object is not valid\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
	for (Py_ssize_t i = 0; i < size + 1 && i < 10; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i == 9 && size + 1 > 10)
			printf("...");
	}
	printf("\n");
}

/**
 * print_python_float - prints float info
 *
 * @p: pyobject
 *
 * Return: void
 */

void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[.] float object is not valid\n");
		return;
	}

	printf("[.] float object info\n");

	value = PyFloat_AsDouble(p);
	printf("  value: %f\n", value);
}
