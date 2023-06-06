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
	listint_t *list1;
	listint_t *list2;

	if (!list || !list->next)
		return (0);
	list1 = list;
	list2 = list;
	while (!list2 && !list2->next)
	{
		list1 = list1->next->next;
		list2 = list2->next;
		if (list1 == list2)
			return (1);
	}
	return (0);
}
