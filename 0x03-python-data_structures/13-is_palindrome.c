#include "lists.h"
#include <stddef.h>

/**
 * reverse_listint - reverses a linked list.
 * @head: head of a list.
 *
 * Return: pointer to the first node.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev;
    listint_t *next;

    prev = NULL;
    next = NULL;

    while (*head != NULL)
    {
        next = (*head)->next;
        (*head)->next = prev;
        prev = *head;
        *head = next;
    }

    *head = prev;
    return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *ptr = *head;
    listint_t *str = *head;

    while (ptr != NULL && str != NULL)
    {
        if (str->next != NULL)
        {
            ptr = ptr->next;
            str = str->next->next;
            if (ptr == str)
            {
                reverse_listint(&str);
                return (1);
            }
        }
    }

    return (0);
}
