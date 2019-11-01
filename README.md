# Distributed System, Lab 9
### Authored by Vyacheslav Shults, B17-DS-1

### RSConfig for the first replica
```
{  
        "_id" : "rs0",  
        "version" : 1,  
        "protocolVersion" : NumberLong(1),  
        "writeConcernMajorityJournalDefault" : true,  
        "members" : [  
                {  
                        "_id" : 0,  
                        "host" : "mongodb1:27017",  
                        "arbiterOnly" : false,  
                        "buildIndexes" : true,  
                        "hidden" : false,  
                        "priority" : 1,  
                        "tags" : {  
  
                        },  
                        "slaveDelay" : NumberLong(0),  
                        "votes" : 1  
                },  
                {  
                        "_id" : 1,  
                        "host" : "mongodb2:27017",  
                        "arbiterOnly" : false,  
                        "buildIndexes" : true,  
                        "hidden" : false,  
                        "priority" : 1,  
                        "tags" : {  
  
                        },  
                        "slaveDelay" : NumberLong(0),  
                        "votes" : 1  
                },  
                {  
                        "_id" : 2,  
                        "host" : "mongodb3:27017",  
                        "arbiterOnly" : false,  
                        "buildIndexes" : true,  
                        "hidden" : false,  
                        "priority" : 1,  
                        "tags" : {  
  
                        },  
                        "slaveDelay" : NumberLong(0),  
                        "votes" : 1  
                }  
        ],  
        "settings" : {  
                "chainingAllowed" : true,  
                "heartbeatIntervalMillis" : 2000,  
                "heartbeatTimeoutSecs" : 10,  
                "electionTimeoutMillis" : 10000,  
                "catchUpTimeoutMillis" : -1,  
                "catchUpTakeoverDelayMillis" : 30000,  
                "getLastErrorModes" : {  
  
                },  
                "getLastErrorDefaults" : {  
                        "w" : 1,  
                        "wtimeout" : 0  
                },  
                "replicaSetId" : ObjectId("5dbb640b1b246ca7d89845e9")  
        }  
}
```

### RSStatus for the first replica
```
{  
        "set" : "rs0",  
        "date" : ISODate("2019-10-31T22:59:43.400Z"),  
        "myState" : 1,  
        "term" : NumberLong(1),  
        "syncingTo" : "",  
        "syncSourceHost" : "",  
        "syncSourceId" : -1,  
        "heartbeatIntervalMillis" : NumberLong(2000),  
        "majorityVoteCount" : 2,  
        "writeMajorityCount" : 2,  
        "optimes" : {  
                "lastCommittedOpTime" : {  
                        "ts" : Timestamp(1572562782, 1),  
                        "t" : NumberLong(1)  
                },  
                "lastCommittedWallTime" : ISODate("2019-10-31T22:59:42.333Z"),  
                "readConcernMajorityOpTime" : {  
                        "ts" : Timestamp(1572562782, 1),  
                        "t" : NumberLong(1)  
                },  
                "readConcernMajorityWallTime" : ISODate("2019-10-31T22:59:42.333Z"),  
                "appliedOpTime" : {  
                        "ts" : Timestamp(1572562782, 1),  
                        "t" : NumberLong(1)  
                },  
                "durableOpTime" : {  
                        "ts" : Timestamp(1572562782, 1),  
                        "t" : NumberLong(1)  
                },  
                "lastAppliedWallTime" : ISODate("2019-10-31T22:59:42.333Z"),  
                "lastDurableWallTime" : ISODate("2019-10-31T22:59:42.333Z")  
        },  
        "lastStableRecoveryTimestamp" : Timestamp(1572562722, 1),  
        "lastStableCheckpointTimestamp" : Timestamp(1572562722, 1),  
        "electionCandidateMetrics" : {  
                "lastElectionReason" : "electionTimeout",  
                "lastElectionDate" : ISODate("2019-10-31T22:45:41.423Z"),  
                "termAtElection" : NumberLong(1),  
                "lastCommittedOpTimeAtElection" : {  
                        "ts" : Timestamp(0, 0),  
                        "t" : NumberLong(-1)  
                },  
                "lastSeenOpTimeAtElection" : {  
                        "ts" : Timestamp(1572561931, 1),  
                        "t" : NumberLong(-1)  
                },  
                "numVotesNeeded" : 2,  
                "priorityAtElection" : 1,  
                "electionTimeoutMillis" : NumberLong(10000),  
                "numCatchUpOps" : NumberLong(27017),  
                "newTermStartDate" : ISODate("2019-10-31T22:45:42.308Z"),  
                "wMajorityWriteAvailabilityDate" : ISODate("2019-10-31T22:45:43.152Z")  
        },  
        "members" : [  
                {  
                        "_id" : 0,  
                        "name" : "mongodb1:27017",  
                        "ip" : "172.31.42.52",  
                        "health" : 1,  
                        "state" : 1,  
                        "stateStr" : "PRIMARY",  
                        "uptime" : 893,  
                        "optime" : {  
                                "ts" : Timestamp(1572562782, 1),  
                                "t" : NumberLong(1)  
                        },  
                        "optimeDate" : ISODate("2019-10-31T22:59:42Z"),  
                        "syncingTo" : "",  
                        "syncSourceHost" : "",  
                        "syncSourceId" : -1,  
                        "infoMessage" : "",  
                        "electionTime" : Timestamp(1572561941, 1),  
                        "electionDate" : ISODate("2019-10-31T22:45:41Z"),  
                        "configVersion" : 1,  
                        "self" : true,  
                        "lastHeartbeatMessage" : ""  
                },  
                {  
                        "_id" : 1,  
                        "name" : "mongodb2:27017",  
                        "ip" : "172.31.23.12",  
                        "health" : 1,  
                        "state" : 2,  
                        "stateStr" : "SECONDARY",  
                        "uptime" : 852,  
                        "optime" : {  
                                "ts" : Timestamp(1572562772, 1),  
                                "t" : NumberLong(1)  
                        },  
                        "optimeDurable" : {  
                                "ts" : Timestamp(1572562772, 1),  
                                "t" : NumberLong(1)  
                        },  
                        "optimeDate" : ISODate("2019-10-31T22:59:32Z"),  
                        "optimeDurableDate" : ISODate("2019-10-31T22:59:32Z"),  
                        "lastHeartbeat" : ISODate("2019-10-31T22:59:41.848Z"),  
                        "lastHeartbeatRecv" : ISODate("2019-10-31T22:59:43.223Z"),  
                        "pingMs" : NumberLong(0),  
                        "lastHeartbeatMessage" : "",  
                        "syncingTo" : "mongodb1:27017",  
                        "syncSourceHost" : "mongodb1:27017",  
                        "syncSourceId" : 0,  
                        "infoMessage" : "",  
                        "configVersion" : 1  
                },  
                {  
                        "_id" : 2,  
                        "name" : "mongodb3:27017",  
                        "ip" : "172.31.16.182",  
                        "health" : 1,  
                        "state" : 2,  
                        "stateStr" : "SECONDARY",  
                        "uptime" : 852,  
                        "optime" : {  
                                "ts" : Timestamp(1572562772, 1),  
                                "t" : NumberLong(1)  
                        },  
                        "optimeDurable" : {  
                                "ts" : Timestamp(1572562772, 1),  
                                "t" : NumberLong(1)  
                        },  
                        "optimeDate" : ISODate("2019-10-31T22:59:32Z"),  
                        "optimeDurableDate" : ISODate("2019-10-31T22:59:32Z"),  
                        "lastHeartbeat" : ISODate("2019-10-31T22:59:41.848Z"),  
                        "lastHeartbeatRecv" : ISODate("2019-10-31T22:59:43.223Z"),  
                        "pingMs" : NumberLong(0),  
                        "lastHeartbeatMessage" : "",  
                        "syncingTo" : "mongodb1:27017",  
                        "syncSourceHost" : "mongodb1:27017",  
                        "syncSourceId" : 0,  
                        "infoMessage" : "",  
                        "configVersion" : 1  
                }  
        ],  
        "ok" : 1,  
        "$clusterTime" : {  
                "clusterTime" : Timestamp(1572562782, 1),  
                "signature" : {  
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),  
                        "keyId" : NumberLong(0)  
                }  
        },  
        "operationTime" : Timestamp(1572562782, 1)  
}
```

![
](https://lh3.googleusercontent.com/NFrrPCux2odXFnWmh2YtbgrwhelmDmWkBQFrk74TXR6AKCBzSm-nUDMnWRFkaaYgW5MSTSCIJ0hy "First screenshot")

### RSConfig for the second replica
```
{  
        "_id" : "rs0",  
        "version" : 1,  
        "protocolVersion" : NumberLong(1),  
        "writeConcernMajorityJournalDefault" : true,  
        "members" : [  
                {  
                        "_id" : 0,  
                        "host" : "mongodb1:27017",  
                        "arbiterOnly" : false,  
                        "buildIndexes" : true,  
                        "hidden" : false,  
                        "priority" : 1,  
                        "tags" : {  
  
                        },  
                        "slaveDelay" : NumberLong(0),  
                        "votes" : 1  
                },  
                {  
                        "_id" : 1,  
                        "host" : "mongodb2:27017",  
                        "arbiterOnly" : false,  
                        "buildIndexes" : true,  
                        "hidden" : false,  
                        "priority" : 1,  
                        "tags" : {  
  
                        },  
                        "slaveDelay" : NumberLong(0),  
                        "votes" : 1  
                },  
                {  
                        "_id" : 2,  
                        "host" : "mongodb3:27017",  
                        "arbiterOnly" : false,  
                        "buildIndexes" : true,  
                        "hidden" : false,  
                        "priority" : 1,  
                        "tags" : {  
  
                        },  
                        "slaveDelay" : NumberLong(0),  
                        "votes" : 1  
                }  
        ],  
        "settings" : {  
                "chainingAllowed" : true,  
                "heartbeatIntervalMillis" : 2000,  
                "heartbeatTimeoutSecs" : 10,  
                "electionTimeoutMillis" : 10000,  
                "catchUpTimeoutMillis" : -1,  
                "catchUpTakeoverDelayMillis" : 30000,  
                "getLastErrorModes" : {  
  
                },  
                "getLastErrorDefaults" : {  
                        "w" : 1,  
                        "wtimeout" : 0  
                },  
                "replicaSetId" : ObjectId("5dbb640b1b246ca7d89845e9")  
        }  
}
```

### RSStatus for the second replica
```
{  
        "set" : "rs0",  
        "date" : ISODate("2019-10-31T23:04:26.488Z"),  
        "myState" : 1,  
        "term" : NumberLong(2),  
        "syncingTo" : "",  
        "syncSourceHost" : "",  
        "syncSourceId" : -1,  
        "heartbeatIntervalMillis" : NumberLong(2000),  
        "majorityVoteCount" : 2,  
        "writeMajorityCount" : 2,  
        "optimes" : {  
                "lastCommittedOpTime" : {  
                        "ts" : Timestamp(1572563063, 1),  
                        "t" : NumberLong(2)  
                },  
                "lastCommittedWallTime" : ISODate("2019-10-31T23:04:23.335Z"),  
                "readConcernMajorityOpTime" : {  
                        "ts" : Timestamp(1572563063, 1),  
                        "t" : NumberLong(2)  
                },  
                "readConcernMajorityWallTime" : ISODate("2019-10-31T23:04:23.335Z"),  
                "appliedOpTime" : {  
                        "ts" : Timestamp(1572563063, 1),  
                        "t" : NumberLong(2)  
                },  
                "durableOpTime" : {  
                        "ts" : Timestamp(1572563063, 1),  
                        "t" : NumberLong(2)  
                },  
                "lastAppliedWallTime" : ISODate("2019-10-31T23:04:23.335Z"),  
                "lastDurableWallTime" : ISODate("2019-10-31T23:04:23.335Z")  
        },  
        "lastStableRecoveryTimestamp" : Timestamp(1572563022, 1),  
        "lastStableCheckpointTimestamp" : Timestamp(1572563022, 1),  
        "electionCandidateMetrics" : {  
                "lastElectionReason" : "stepUpRequestSkipDryRun",  
                "lastElectionDate" : ISODate("2019-10-31T23:01:32.421Z"),  
                "termAtElection" : NumberLong(2),  
                "lastCommittedOpTimeAtElection" : {  
                        "ts" : Timestamp(1572562892, 1),  
                        "t" : NumberLong(1)  
                },  
                "lastSeenOpTimeAtElection" : {  
                        "ts" : Timestamp(1572562892, 1),  
                        "t" : NumberLong(1)  
                },  
                "numVotesNeeded" : 2,  
                "priorityAtElection" : 1,  
                "electionTimeoutMillis" : NumberLong(10000),  
                "priorPrimaryMemberId" : 0,  
                "numCatchUpOps" : NumberLong(180834000),  
                "newTermStartDate" : ISODate("2019-10-31T23:01:33.329Z"),  
                "wMajorityWriteAvailabilityDate" : ISODate("2019-10-31T23:01:34.410Z")  
        },  
        "members" : [  
                {  
                        "_id" : 0,  
                        "name" : "mongodb1:27017",  
                        "ip" : "172.31.42.52",  
                        "health" : 0,  
                        "state" : 8,  
                        "stateStr" : "(not reachable/healthy)",  
                        "uptime" : 0,  
                        "optime" : {  
                                "ts" : Timestamp(0, 0),  
                                "t" : NumberLong(-1)  
                        },  
                        "optimeDurable" : {  
                                "ts" : Timestamp(0, 0),  
                                "t" : NumberLong(-1)  
                        },  
                        "optimeDate" : ISODate("1970-01-01T00:00:00Z"),  
                        "optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),  
                        "lastHeartbeat" : ISODate("2019-10-31T23:04:20.427Z"),  
                        "lastHeartbeatRecv" : ISODate("2019-10-31T23:01:31.889Z"),  
                        "pingMs" : NumberLong(0),  
                        "lastHeartbeatMessage" : "Couldn't get a connection within the time limit",  
                        "syncingTo" : "",  
                        "syncSourceHost" : "",  
                        "syncSourceId" : -1,  
                        "infoMessage" : "",  
                        "configVersion" : -1  
                },  
                {  
                        "_id" : 1,  
                        "name" : "mongodb2:27017",  
                        "ip" : "172.31.23.12",  
                        "health" : 1,  
                        "state" : 1,  
                        "stateStr" : "PRIMARY",  
                        "uptime" : 1202,  
                        "optime" : {  
                                "ts" : Timestamp(1572563063, 1),  
                                "t" : NumberLong(2)  
                        },  
                        "optimeDate" : ISODate("2019-10-31T23:04:23Z"),  
                        "syncingTo" : "",  
                        "syncSourceHost" : "",  
                        "syncSourceId" : -1,  
                        "infoMessage" : "",  
                        "electionTime" : Timestamp(1572562892, 2),  
                        "electionDate" : ISODate("2019-10-31T23:01:32Z"),  
                        "configVersion" : 1,  
                        "self" : true,  
                        "lastHeartbeatMessage" : ""  
                },  
                {  
                        "_id" : 2,  
                        "name" : "mongodb3:27017",  
                        "ip" : "172.31.16.182",  
                        "health" : 1,  
                        "state" : 2,  
                        "stateStr" : "SECONDARY",  
                        "uptime" : 1134,  
                        "optime" : {  
                                "ts" : Timestamp(1572563063, 1),  
                                "t" : NumberLong(2)  
                        },  
                        "optimeDurable" : {  
                                "ts" : Timestamp(1572563063, 1),  
                                "t" : NumberLong(2)  
                        },  
                        "optimeDate" : ISODate("2019-10-31T23:04:23Z"),  
                        "optimeDurableDate" : ISODate("2019-10-31T23:04:23Z"),  
                        "lastHeartbeat" : ISODate("2019-10-31T23:04:26.430Z"),  
                        "lastHeartbeatRecv" : ISODate("2019-10-31T23:04:26.414Z"),  
                        "pingMs" : NumberLong(0),  
                        "lastHeartbeatMessage" : "",  
                        "syncingTo" : "mongodb2:27017",  
                        "syncSourceHost" : "mongodb2:27017",  
                        "syncSourceId" : 1,  
                        "infoMessage" : "",  
                        "configVersion" : 1  
                }  
        ],  
        "ok" : 1,  
        "$clusterTime" : {  
                "clusterTime" : Timestamp(1572563063, 1),  
                "signature" : {  
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),  
                        "keyId" : NumberLong(0)  
                }  
        },  
        "operationTime" : Timestamp(1572563063, 1)  
}
```

![
](https://lh3.googleusercontent.com/eHHf2ifYNnAEPRuSBNHWl555-jX_i9Mm77nJCnq7q7u4AVMdrVE4ej5I4wv7GsbVEw931GHBYjRS "Second screenshot")
