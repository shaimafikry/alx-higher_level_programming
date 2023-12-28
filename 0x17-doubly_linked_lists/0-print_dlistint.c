#include "lists.h"
/**
 * print_dilistint - prints list
 * @h: pointer to the head
 * Return: num of list elemnts
*/
size_t print_dlistint(const dlistint_t *h)
{
	int i = 0; /*for counting*/
	dlistint_t *current;

	current = h;
	if (current == NULL)
		return (0);
	
	while (current != NULL)
	{
		printf("%d\n",current->n);
		current = current->next;
		i++;
	}

	return (i);
	
}
