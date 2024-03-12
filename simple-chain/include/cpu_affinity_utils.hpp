#ifndef CPU_AFFINITY_UTILS_HPP
#define CPU_AFFINITY_UTILS_HPP

#include <string>
#include <map>
#include <pthread.h>

/*
    Load affinity settings from a yaml file.
*/
std::map<std::string, int> load_thread_affinities(const std::string& file_path);

/*

*/
void setThreadAffinity(int core_id);

/*

*/
void checkThreadAffinity(pthread_t thread);

#endif //CPU_AFFINITY_UTILS_HPP