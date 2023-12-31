#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;
	listint_t *str = list;

	while (ptr != NULL && str != NULL)

		if (str->next != NULL)
		{
			ptr = ptr->next;
			str = str->next->next;
			if (ptr == str)
			{
				return (1);
			}
		}
	return (0);
}


