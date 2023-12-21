#include "lists.h"
/**
 * check_cycle - hecks if linked list is cycled or not
 * @list: linked list "head"
 * Return: 1 if it is , 0 if it is not
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	while (fast != NULL && fast->next != NULL)
	{
	slow = slow->next;
	fast = fast->next->next;
	if (slow == fast)
	{
		return (1);
	}
	}
	return (0);
}
