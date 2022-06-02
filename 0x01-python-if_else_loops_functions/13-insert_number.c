#include "lists.h"

/**
  * insert_node - Inserts a no. into a soorted linked list.
  * @head: 1st node in the list.
  * @number: No. Inserted into the list.
  *
  * Return: Pointer to Inserted node or NULL on failure.
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *temp;

	if (!*head)
	{
		node = add_nodeint_end(head, number);
		return (node);
	}

	if ((*head)->n > number)
	{
		node = malloc(sizeof(listint_t));
		if (!node)
			return (0);
		node->next = *head;
		node->n = number;
		*head = node;
		return (*head);
	}

	while (node)
	{
		if (!node->next)
		{
			node->next = insert_node(&node->next, number);
			break;
		}
		if (node->next->n > number)
		{
			temp = malloc(sizeof(listint_t));
			if (!temp)
				return (0);
			temp->next = node->next;
			temp->n = number;
			node->next = temp;

			break;
		}
		node = node->next;
	}
	return (node);
}
