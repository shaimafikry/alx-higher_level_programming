#include "lists.h"

/**
 * is_palindrome - to check if its start equal its end
 * @head: a pointer to the first node
 * Return: 1 if it's pal 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *current, *first, *end, *prev;

	if (*head == NULL)
		return (1);
	current = *head;
	current = malloc(sizeof(listint_t));
	first = malloc(sizeof(listint_t));
	end = malloc(sizeof(listint_t));
	prev = malloc(sizeof(listint_t));
	first->n = current->n;
	while (current != NULL)
	{
		end->n = current->n;
		current = current->next;
	}
	current = *head;
	while(current != NULL)
	{
		if (first->n == end->n)
		{
			current = current->next;
			first->n = current->n;
			prev = current;
			while (prev != NULL)
			{
				end->n = prev->n;
				prev = prev->next;
			}
		}
		else 
		{
			free(current);
			free(prev);
			free(first);
			free(end);
			return (0);
		}
	}
	free(current);
	free(prev);
	free(first);
	free(end);
	return (1);
}
