#include "lists.h"
/**
 * check_cycle - hecks if linked list is cycled or not
 * @list: linked list "head"
 * Return: 1 if it is , 0 if it is not
*/
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *prev;

	current = list;
	prev = NULL;
	while (current != NULL)
	{
		if (current == prev)
			return (1);
		prev = current;
		current = current->next;
	}
	return (0); /*linked list is cycle*/
}
