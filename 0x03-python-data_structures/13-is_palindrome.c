#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: The first item oin the list
 *
 * Return: (int) 1 if it's a palindrome, 0 if it isn't
 */

int is_palindrome(listint_t **head)
{
	int list_int[1024], i, n, array_size = 0;
	listint_t *temp;

	if (*head == NULL)
		return (1);
	temp = *head;
	for (i = 0; temp != NULL; i++)
	{
		list_int[i] = temp->n;
		temp = temp->next;
	}
	for (i = 0; list_int[i]; i++)
		array_size++;
	for (i = 0, n = array_size - 2; n != i - 1; i++, n--)
	{
		if (n == i - 2)
			break;
		if (list_int[i] != list_int[n])
			return (0);
	}
	return (1);
}
