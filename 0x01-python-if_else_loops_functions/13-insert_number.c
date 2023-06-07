#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: THe linked list
 * @number: the number to be added
 *
 * Return: char pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp;

	new_node = malloc(sizeof(listint_t));
        if (new_node == NULL)
                return (NULL);
        new_node->n = number;

	temp = *head;
	if (temp == NULL || number < temp->n)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}
	while (temp->next != NULL && temp->next->n < number)
		temp = temp->next;
	new_node->next = temp->next;
	temp->next = new_node;
	return (new_node);
}
