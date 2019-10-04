#!/usr/bin/env python3
#Tinsae Debele  # 101034827
import sqlite3
dbconnect = sqlite3.connect("lab4.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
cursor.execute('''insert into sensors values (4, 'motion', 'garage')''');
dbconnect.commit();

# Kitchen sensors
cursor.execute('''SELECT * FROM sensors WHERE zone IS 'kitchen' ''');
print("---- Kitchen Sensors ----")
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );


cursor.execute('''SELECT * FROM sensors WHERE type IS 'door' ''');
print("---- Door Sensors ----")
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] )
#close the connection
dbconnect.close();
