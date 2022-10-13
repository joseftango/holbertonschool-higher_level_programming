#include "lists.h"
/**
* insert_node - inserts a number into a sorted linked list
* @head: double pointer to a list
* @number: integer
* Return: address of the new node
**/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *traversal, *pre_traversal, *new_node;

	if (!head || !(*head))
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	traversal = (*head)->next;
	pre_traversal = *head;

	while (traversal)
	{
		if (traversal->n > new_node->n)
		{
			new_node->next = traversal;
			pre_traversal->next = new_node;
			break;
		}

		if (pre_traversal->n > new_node->n)
		{
			new_node->next = pre_traversal;
			break;
		}

		traversal = traversal->next;
		pre_traversal = pre_traversal->next;

	}

	return (new_node);
}
