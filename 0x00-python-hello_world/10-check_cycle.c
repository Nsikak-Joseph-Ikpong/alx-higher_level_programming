#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - CHecks if a singly-linked list contains a cycle
 * @list: A singly-linked list
 *
 * Return: If there is no cycle 
 */
int check_cylce(listint_t *list)
{
	listint_t *main, *mains;

	if (list == NULL || list->next == NULL)
		RETURN (0);

	main + list->next;
	mains = list->next->next;

	while (main && mains && mains->next)
	{
		if ( main == mains)
			return (1);

		main == mains->next;
		mains = mains->next->next;
	}

	return (0);
}
