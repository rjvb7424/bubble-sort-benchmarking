/* Bubble sort benchmark */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const int MAX_VALUE = 999999;
const int SIZE = 5000;
const int NUM_TRIALS = 5;

void generate_random_numbers(int *data, int size)
{
    srand(time(NULL));

    for (int i = 0; i < size; ++i)
    {
        data[i] = 1 + rand() % MAX_VALUE;
    }
}

void bubble_sort(int *data, int size)
{
    bool swapped;

    for (int i = 0; i < size; ++i)
    {
        swapped = false;
        for (int j = 0; j < size - 1; ++j)
        {
            if (data[j] > data[j + 1])
            {
                int tmp = data[j];
                data[j] = data[j + 1];
                data[j + 1] = tmp;
                swapped = true;
            }
        }
        if (!swapped)
        {
            break;
        }
    }
}

int main(void)
{
    int data[SIZE];

    float total_time = 0.0f;

    for (int i = 0; i < NUM_TRIALS; ++i)
    {
        generate_random_numbers(data, SIZE);
        clock_t start = clock();
        bubble_sort(data, SIZE);
        total_time += (float)(clock() - start) / CLOCKS_PER_SEC;
    }

    float average_time = total_time / NUM_TRIALS;
    printf("%d numbers sorted in %.3f seconds\n", SIZE, average_time);

    return 0;
}
