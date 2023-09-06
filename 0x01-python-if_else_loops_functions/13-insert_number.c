#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * insert_node - inserts a new node
 * at a given position.
 * @head: head of a list.
 * @number: index of the list where the new node is
 * added.
 * Return: the address of the new node, or NULL if it
 * failed.
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *new = *head, *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	{
		new->n = number;
		new->next = NULL;
		new->next = *head;
		*head = new;
		return (new);
	}
	temp = *head;
	while (temp != NULL)
	{
		temp = temp->next;

	}

	if (temp != NULL)
	{
		return (NULL);
	}

	new->n = number;
	new->next = temp->next;
	temp->next = new;
	return (new);
}
