#include "lists.h"
/**
* reverse_list - function that reverse a singly linked list
* @head: pointer to first node of a list
* Return: pointer to the reversed list
**/

listint_t *reverse_list(listint_t *head)
{
	listint_t *next = NULL, *prev = NULL;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;

	}
	head = prev;
	return (head);
}


/**
* is_palindrome - function that checks whether list is palindrome
* @head: double pointer to a list
* Return: 1 if success 0 if fail
**/

int is_palindrome(listint_t **head)
{
listint_t *traversal, *first_half, *second_half, *rev_second_half;
int len = 0, count = 0, len_both = 0;

	if (!head || !(*head))
		return (0);

	traversal = *head;

	while (traversal != NULL)
	{
		len++;
		traversal = traversal->next;
	}

	if (len % 2 != 0)
		return (0);

	len_both = len / 2;

	first_half = *head;
	second_half = *head;

	while (second_half != NULL)
	{
		if (count == len_both)
		{
			second_half = second_half->next;
			break;
		}

		count++;
		second_half = second_half->next;
	}

	rev_second_half = reverse_list(second_half);
	count = 0;

	while (first_half != NULL && rev_second_half != NULL)
	{
		if (first_half->n != rev_second_half->n)
			return (0);

	first_half = first_half->next;
	rev_second_half = rev_second_half->next;

	}

	return (1);
}
