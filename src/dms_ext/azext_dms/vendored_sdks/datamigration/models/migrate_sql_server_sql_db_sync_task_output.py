# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MigrateSqlServerSqlDbSyncTaskOutput(Model):
    """Output for the task that migrates on-prem SQL Server databases to Azure SQL
    Database for online migrations.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: MigrateSqlServerSqlDbSyncTaskOutputDatabaseError,
    MigrateSqlServerSqlDbSyncTaskOutputError,
    MigrateSqlServerSqlDbSyncTaskOutputTableLevel,
    MigrateSqlServerSqlDbSyncTaskOutputDatabaseLevel,
    MigrateSqlServerSqlDbSyncTaskOutputMigrationLevel

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Constant filled by server.
    :type result_type: str
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
    }

    _subtype_map = {
        'result_type': {'DatabaseLevelErrorOutput': 'MigrateSqlServerSqlDbSyncTaskOutputDatabaseError', 'ErrorOutput': 'MigrateSqlServerSqlDbSyncTaskOutputError', 'TableLevelOutput': 'MigrateSqlServerSqlDbSyncTaskOutputTableLevel', 'DatabaseLevelOutput': 'MigrateSqlServerSqlDbSyncTaskOutputDatabaseLevel', 'MigrationLevelOutput': 'MigrateSqlServerSqlDbSyncTaskOutputMigrationLevel'}
    }

    def __init__(self):
        super(MigrateSqlServerSqlDbSyncTaskOutput, self).__init__()
        self.id = None
        self.result_type = None
