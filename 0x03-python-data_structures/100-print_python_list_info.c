/**
  * print_python_list_info - Prints basic information
  * about Python Lists.
  * @p: Pointer to a python object.
  */
void print_python_list_info(PyObject *p)
{
	int i, list_length;
	PyObject *object;
	PyListObject *listObject = (PyListObject *) p;

	list_length = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", list_length);
	printf("[*] Allocated = %d\n", (int)listObject->allocated);

	for (i = 0; i < list_length; ++i)
	{
		object = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, object->ob_type->tp_name);
	}
}
