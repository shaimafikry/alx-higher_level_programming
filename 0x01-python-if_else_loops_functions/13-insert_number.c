#include "lists.h"
/**
 * insert_node: insterts a node in a sorted linked list
 * @head: first in linked list
 * @number: number to be added
 * @Return: pointer to a new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *loop;
	listint_t *new;
	int check;

	if (head == NULL)
	{
		return (NULL);
	}
	loop = malloc(sizeof(listint_t));
	if (loop == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	loop = *head;
	check = loop->n;/*first value in linked list*/
	while (loop->next != NULL)
	{
		if (number >= check)
		{
			new->next = loop;
			loop = new;
		}
		loop = loop->next;
	}
	return (new); 
}
