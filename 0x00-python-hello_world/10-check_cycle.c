#include "lists.h"
/**
 * check_cycle - hecks if linked list is cycled or not
 * @list: linked list "head"
 * Return: 1 if it is , 0 if it is not
*/
int check_cycle(listint_t *list)
{

	listint_t *loop;
	int check, num;

	loop = malloc(sizeof(listint_t));
	if (loop == NULL)
		return (-1);

	check = list->n;/*first value in linked list*/
	loop = list->next;
	num = loop->n;/*second value in linked list*/
	while (check != num)
	{
		loop = loop->next;/*loops threoug lists*/
		if (loop  == NULL)
			return (0); /*linked list is not cycle*/
		num = loop->n;
	}
	return (1); /*linked list is cycle*/
}
