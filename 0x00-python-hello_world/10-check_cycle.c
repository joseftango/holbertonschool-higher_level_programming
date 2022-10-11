#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: the given list
* Return: 1 or 0
**/

int check_cycle(listint_t *list)
{
	listint_t *traversal = list, *holder = list;

	if (!list || !list->next)
		return (0);

	while (holder)
	{
		traversal = traversal->next;
		holder = holder->next->next;

		if (traversal == holder)
			return (1);
	}

	return (0);
}
