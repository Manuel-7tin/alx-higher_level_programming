#include "lists.h"

/**
 * check_cycle - Checks if a linked  has a cycle i it
 *
 * @list: The list to be checked
 *
 * Return: int, 1 if it has, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	if (list->next)
		return (1);
	else
		return (0);
}
