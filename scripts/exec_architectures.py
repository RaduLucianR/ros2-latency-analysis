def exec_architectures():
    return [ 
        ################# 2 NODES ###############
        ##### 2 NODES - 1 exec - s
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
        ######## 3 NODES - 1 exec - s
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 1 exec - m
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 3 exec - sss - 11223
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 3 exec - mmm - 11223
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 3 exec - ssm - 11223
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 3 exec - mms - 11223
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 3 exec - sss - 11123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 3 exec - mmm - 11123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 3 exec - ssm - 11123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },
        
        ######## 5 NODES - 3 exec - mms - 11123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 5 exec - sssss
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
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
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        #############
        ######## 5 NODES - 5 exec - mmmmm
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
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
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 5 NODES - 5 exec - sssmm
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
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
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
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ##########################
        ######## 5 NODES - 5 exec - mmmss
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
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
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
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 6 NODES - 1 exec - s
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"},
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"},
                    ],
                }
            ]
        },

        ######## 6 NODES - 2 exec - ss - 111222
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 6 NODES - 2 exec - mm - 111222
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 6 NODES - 2 exec - sm - 111222
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 6 NODES - 2 exec - ss - 111112
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 6 NODES - 2 exec - mm - 111112
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 6 NODES - 2 exec - sm - 111112
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 6 NODES - 2 exec - ms - 111112
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },  
        
        ######### 6 NODES - 2 exec - ss - 111122
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },      

        ######### 6 NODES - 2 exec - mm - 111122
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 2 exec - sm - 111122
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },   

        ######### 6 NODES - 2 exec - ms - 111122
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },
        
        ######### 6 NODES - 3 exec - sss - 112233
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 3 exec - mmm - 112233
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 3 exec - ssm - 112233
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 3 exec - mms - 112233
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 3 exec - sss - 111123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 3 exec - mmm - 111123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 3 exec - ssm - 111123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 3 exec - mms - 111123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 4 exec - ssss - 112234
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 4 exec - mmmm - 112234
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 4 exec - ssmm - 112234
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 4 exec - mmss - 112234
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 6 exec - ssssss
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 6 exec - mmmmmm
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######### 6 NODES - 6 exec - sssmmm
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
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
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
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 1 exec - s
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"},
                    ],
                }
            ]
        },

        ######## 7 NODES - 1 exec - m
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"},
                    ],
                }
            ]
        },

        ######## 7 NODES - 3 execs - sss - 1112233
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 3 execs - mmm - 1112233
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 3 execs - ssm - 1112233
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 3 execs - mms - 1112233
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 3 execs - sss - 1111123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 3 execs - mmm - 1111123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 3 execs - ssm - 1111123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 3 execs - mms - 1111123
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 5 exec - sssss - 1122345
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 5 exec - mmmmm - 1122345
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 5 exec - sssmm - 1122345
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 5 exec - mmmss - 1122345
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 5 exec - sssss - 1112345
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 5 exec - mmmmm - 1112345
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 5 exec - sssmm - 1112345
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 7 NODES - 5 exec - mmmss - 1112345
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ####### 7 NODES - 7 exec - sssssss
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor7",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor7",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ####### 7 NODES - 7 exec - mmmmmmm
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor7",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor7",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ####### 7 NODES - 7 exec - ssssmmm
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor7",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor7",
                    "type": "multi_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ####### 7 NODES - 7 exec - mmmmsss
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor7",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
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
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor7",
                    "type": "single_threaded",
                    "cores": [3],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 8 NODES - 1 exec - s
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"},
                    ],
                }
            ]
        },

        ######## 8 NODES - 1 exec - m
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"},
                    ],
                }
            ]
        },

        ######## 8 NODES - 2 exec - ss - 11112222
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 8 NODES - 2 exec - mm - 11112222
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 8 NODES - 2 exec - sm - 11112222
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },


        ###############

        ######## 8 NODES - 2 exec - ss - 11111122
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 8 NODES - 2 exec - mm - 11112222
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 8 NODES - 2 exec - sm - 11112222
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
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
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "multi_threaded",
                    "cores": [2],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 8 NODES - 4 exec - ssss
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 8 NODES - 6 exec - ssssss
        {
            "executors": [
                {
                    "name": "executor1",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": "128B"},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor2",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": "128B"},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor3",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor4",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor5",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"}
                    ],
                },

                {
                    "name": "executor6",
                    "type": "single_threaded",
                    "cores": [1],
                    "nodes": [
                        {"name": "node8", "subscribe": "topic7", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },

        ######## 9 NODES - 1 exec - s
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "topic8", "payload": "128B"},
                        {"name": "node9", "subscribe": "topic8", "publish": "NONE", "payload": "128B"},
                    ],
                }
            ]
        },

        ######## 9 NODES - 1 exec - m
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "topic8", "payload": "128B"},
                        {"name": "node9", "subscribe": "topic8", "publish": "NONE", "payload": "128B"},
                    ],
                }
            ]
        },

        ######## 10 NODES - 1 exec - s
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "topic8", "payload": "128B"},
                        {"name": "node9", "subscribe": "topic8", "publish": "topic9", "payload": "128B"},
                        {"name": "node10", "subscribe": "topic9", "publish": "NONE", "payload": "128B"},
                    ],
                }
            ]
        },

        ######## 10 NODES - 1 exec - m
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
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": "128B"},
                        {"name": "node5", "subscribe": "topic4", "publish": "topic5", "payload": "128B"},
                        {"name": "node6", "subscribe": "topic5", "publish": "topic6", "payload": "128B"},
                        {"name": "node7", "subscribe": "topic6", "publish": "topic7", "payload": "128B"},
                        {"name": "node8", "subscribe": "topic7", "publish": "topic8", "payload": "128B"},
                        {"name": "node9", "subscribe": "topic8", "publish": "topic9", "payload": "128B"},
                        {"name": "node10", "subscribe": "topic9", "publish": "NONE", "payload": "128B"}
                    ],
                }
            ]
        },
    ]