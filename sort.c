/* Bubble sort benchmark with increasing list sizes */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_VALUE 999999
#define MAX_SIZE 400 // Match LIST_SIZE in Python
#define NUM_TRIALS 5

// Function to generate random numbers
void generate_random_numbers(int *data, int size)
{
    for (int i = 0; i < size; ++i)
    {
        data[i] = 1 + rand() % MAX_VALUE;
    }
}

// Bubble sort implementation
void bubble_sort(int *data, int size)
{
    bool swapped;
    for (int i = 0; i < size; ++i)
    {
        swapped = false;
        for (int j = 0; j < size - 1 - i; ++j)
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

// Benchmark runner
int main(void)
{
    srand(time(NULL));                            // Seed once
    FILE *f = fopen("c_bubble_results.csv", "w"); // Save results to CSV
    if (!f)
    {
        perror("File open failed");
        return 1;
    }

    fprintf(f, "ListSize,AverageTime\n");

    int *data = malloc(sizeof(int) * MAX_SIZE);
    if (!data)
    {
        perror("Memory allocation failed");
        fclose(f);
        return 1;
    }

    for (int size = 0; size < MAX_SIZE; ++size)
    {
        float total_time = 0.0f;

        for (int trial = 0; trial < NUM_TRIALS; ++trial)
        {
            generate_random_numbers(data, size);
            clock_t start = clock();
            bubble_sort(data, size);
            total_time += (float)(clock() - start) / CLOCKS_PER_SEC;
        }

        float average_time = total_time / NUM_TRIALS;
        fprintf(f, "%d,%.6f\n", size, average_time);
    }

    free(data);
    fclose(f);
    printf("C benchmark completed and saved to c_bubble_results.csv\n");
    return 0;
}
