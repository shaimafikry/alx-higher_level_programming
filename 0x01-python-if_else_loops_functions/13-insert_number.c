#include "lists.h"
/**
 * insert_node - insterts a node in a sorted linked list
 * @head: first in linked list
 * @number: number to be added
 * Return: pointer to a new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *loop;
	listint_t *new;

	if (head == NULL)
	{
		return (NULL);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		loop = *head;
		while (loop->next != NULL && loop->next->n < number)
			loop = loop->next;
		new->next = loop->next;
		loop->next = new;
	}
	return (new);
}
