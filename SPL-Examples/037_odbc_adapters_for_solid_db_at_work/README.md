This example shows the use of the three Streams ODBC adapters for connecting to a SolidDB in-memory database. Those operators are ODBCSource, ODBCAppend, and ODBCEnrich. The code in this example is written to access a particular test SolidDB database inside IBM. You have to create your own SolidDB database and tables to make this application work in your environment.

After creating your own database and tables, you have to change the ./etc/connections.xml file in this application's directory to match your database/table names, userid, and password. You also have to make changes in the SPL code using your database information for all the three ODBC operator invocations.

