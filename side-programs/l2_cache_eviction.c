#include <stdio.h>
#include <pthread.h>
#include <sched.h>

int main()
{
    int s, cpu;
    cpu_set_t cpuset;
    pthread_t thread;

    thread = pthread_self();     // Get the ID of the current thread

    CPU_ZERO(&cpuset);           // Clear all entries from the CPU set
    CPU_SET(3, &cpuset);         // Add CPU 0 to the CPU set

    // Set affinity of the current thread to the defined CPU set
    s = pthread_setaffinity_np(thread, sizeof(cpu_set_t), &cpuset);
    if (s != 0) {
        perror("pthread_setaffinity_np");
        return 1;
    }

    CPU_ZERO(&cpuset);

    // Retrieve the affinity mask for the current thread
    s = pthread_getaffinity_np(thread, sizeof(cpu_set_t), &cpuset);
    if (s != 0) {
        perror("pthread_getaffinity_np");
        return 1;
    }

    // Iterate through the CPU set and print the CPUs on which the thread can run
    printf("Current thread is set to run on the following CPUs: ");
    for (cpu = 0; cpu < CPU_SETSIZE; cpu++) {
        if (CPU_ISSET(cpu, &cpuset)) {
            printf("%d ", cpu);
        }
    }
    
    printf("\n");

    int L2_CACHE_SIZE = 1048576;
    char a[L2_CACHE_SIZE];

    while (1) {
        for (int i = 0; i < L2_CACHE_SIZE; i++) {
            a[i] = a[i] + 1;
            printf("Hey %d\n", i);
        }
    }
}