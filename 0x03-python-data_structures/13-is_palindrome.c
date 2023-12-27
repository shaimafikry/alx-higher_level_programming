#include "lists.h"

/**
 * is_palindrome - to check if its start equal its end
 * @head: a pointer to the first node
 * Return: 1 if it's pal 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *current, *first, *end, *check;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	first = current;
	end = current;
	while (end->next!= NULL)
		end = end->next;
	while(current != NULL)
	{		
		if (first->n == end->n)
		{
			current = current->next;
			first = current;
			end = current;
		}
		else
			return (0);
		check = end;
		while (check->next->next!= NULL)
			{
				end = end->next;
				check = end;
			}
			end->next = NULL;

	
	}
	return (1);
}
