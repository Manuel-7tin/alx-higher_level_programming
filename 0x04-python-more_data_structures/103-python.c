#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints info about python lissts
 *
 * @p: a pythn object
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t index;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (index = 0; index < size; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints info about python bytes
 *
 * @p: a pythn object
 *
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	char *string;

	if (!PyBytes_Check(p))
	{
		printf("Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	if (size > 10)
		size = 10;

	string = PyBytes_AsString(p);

	printf("  trying string: %s\n", string);

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)string[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
