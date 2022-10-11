#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: the given list
* Return: 1 or 0
**/

int check_cycle(listint_t *list)
{
	listint_t *traversal = list->next;

	if (!list || !list->next)
		return (0);

	while (traversal != NULL)
	{
		if (traversal == list)
			return (1);
		traversal = traversal->next;
	}

	return (0);
}
