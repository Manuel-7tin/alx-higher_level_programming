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

	if (*head == NULL || (*head)->next == NULL)
		return (NULL);
	temp = *head;
	while (temp->next->n < number && temp->next != NULL)
		temp = temp->next;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = temp->next;
	temp->next = new_node;
	return (new_node);
}
