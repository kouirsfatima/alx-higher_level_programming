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
    listint_t *prev = NULL;
    listint_t *next = NULL;

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
    
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (ptr != NULL && str != NULL)
    {
        if (str->next != NULL)
        {
            ptr = ptr->next;
            str = str->next->next;
            if (ptr == str)
            {
                reverse_listint(&str);
                break;
            }
        }
        else
        {
            ptr = NULL;
        }
    }

    ptr = *head;
    while (str != NULL)
    {
        if (ptr->n != str->n)
            return (0); 
        ptr = ptr->next;
        str = str->next;
    }

    return (1); // It is a palindrome
}

/**
 * comparelist - compares two linked lists for equality
 *
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int comparelist(listint_t *head1, listint_t *head2)
{
    listint_t *temp1 = head1;
    listint_t *temp2 = head2;

    while (temp1 != NULL && temp2 != NULL)
    {
        if (temp1->n != temp2->n)
        {
            return 0;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    if (temp1 == NULL && temp2 == NULL)
    {
        return 1; 
    }

    return 0;
}
