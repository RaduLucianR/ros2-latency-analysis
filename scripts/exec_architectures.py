def exec_architectures():
    return [ 
        ################# 2 NODES ###############
        ##### 2 NODES - 1 exec
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ##### 2 NODES - 2 exec
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ################# 3 NODES ###############
        ######## 3 NODES - 1 exec
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 3 NODES - 2 execs
        ######## 3 NODES - 2 execs - ss
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 3 NODES - 2 execs - mm
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 3 NODES - 2 execs - sm
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 3 NODES - 2 execs - ms
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 3 NODES - 3 execs
        ######## 3 NODES - 3 execs - sss
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 3 NODES - 3 execs - mmm
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 3 NODES - 3 execs - ssm
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 3 NODES - 3 execs - mms
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ################# 4 NODES ###############
        ######## 4 NODES - 1 exec - s
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 1 exec - m
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 2 execs - ss - 1122
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 2 execs - ss - 1112
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ### 4 NODES - 2 execs - mm
        ######## 4 NODES - 2 execs - mm - 1122
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 2 execs - mm - 1112
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        #### 4 NODES - 2 execs - sm - 1122
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 2 execs - sm - 1112
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        #### 4 NODES - 2 execs - ms - 1122
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 2 execs - ms - 1112
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 4 execs - ssss
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [0],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 4 execs - mmmm
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [0],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 4 execs - ssmm
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [0],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 4 NODES - 4 execs - mmss
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [0],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 1 exec - s
    ]