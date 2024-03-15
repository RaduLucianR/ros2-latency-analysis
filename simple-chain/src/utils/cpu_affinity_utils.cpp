#include "cpu_affinity_utils.hpp"
#include <sched.h>
#include <yaml-cpp/yaml.h>
#include <vector>
#include <thread>
#include <iostream>
#include <unistd.h>
#include "rcutils/logging_macros.h"

std::map<std::string, int> load_thread_affinities(const std::string& file_path) {
    YAML::Node config = YAML::LoadFile(file_path);
    std::map<std::string, int> thread_affinities;

    for (const auto& thread_config : config) {
        std::string thread_name = thread_config.first.as<std::string>();
        int core_id = thread_config.second["core"].as<int>();
        thread_affinities[thread_name] = core_id;
    }

    return thread_affinities;
}

void setThreadAffinity(int core_id) {
    int num_cores = sysconf(_SC_NPROCESSORS_ONLN);

    if (core_id < 0 || core_id >= num_cores)
        RCUTILS_LOG_ERROR("Affinity out of range!");

    cpu_set_t cpuset;
    CPU_ZERO(&cpuset);
    CPU_SET(core_id, &cpuset);

    pthread_t current_thread = pthread_self();
    int rc = pthread_setaffinity_np(current_thread, sizeof(cpu_set_t), &cpuset);

    if (rc != 0) {
        // std::cerr << "Error setting thread affinity: " << rc << std::endl;
        RCUTILS_LOG_ERROR("Error setting thread affinity!");
    }

    CPU_ZERO(&cpuset);
    pthread_getaffinity_np(current_thread, sizeof(cpu_set_t), &cpuset);

    for (int cpu = 0; cpu < CPU_SETSIZE; cpu++) {
        if (CPU_ISSET(cpu, &cpuset)) {
            // std::cout << " CPU" << cpu;
            RCUTILS_LOG_INFO("Thread %lu has affinity: CPU%d", current_thread, cpu);
        }
    }
}