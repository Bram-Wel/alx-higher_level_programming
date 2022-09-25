#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Check a linked list for a cycle.
  * @list: Pointer to the List.
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *node, *temp;

	node = list;
	temp = list;

	while (node)
	{
		if (temp && temp->next)
		{
			temp = temp->next->next;

			if (node == temp)
				return (1);
		}
		node = node->next;
	}
	return (0);
}
