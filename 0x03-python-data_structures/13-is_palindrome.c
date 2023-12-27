#include "lists.h"

/**
 * is_palindrome - to check if its start equal its end
 * @head: a pointer to the first node
 * Return: 1 if it's pal 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *current;

	current = malloc(sizeof(listint_t));
	if (*head == NULL)
		return (1);
	current->n = (*head)->n;
	while ((*head)->next != NULL)
	{
		*head = (*head)->next;
	}
	if ((*head)->n == current->n)
		return (1);
	else
		return (0);
}
