#include "lists.h"

/**
 * is_palindrome - to check if its start equal its end
 * @head: a pointer to the first node
 * Return: 1 if it's pal 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *current, *first, *end;
	size_t  t = 0, m = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	first = current;
	while (current != NULL)
	{
		end = current;
		current = current->next;
		m++;
	}
	current = *head;
	while(current != NULL)
	{
		t++;
		
		if (first->n == end->n)
		{
			if (t == m/2)
				break;
			current = current->next;
			first = current;
			end = current;
			while (end->next->next != NULL)
			{
				end = end->next;
			}
			end->next= NULL;
		}
		else 
		{
			return (0);
		}
	}
	return (1);
}
