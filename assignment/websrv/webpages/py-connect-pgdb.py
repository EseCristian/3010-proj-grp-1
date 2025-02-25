#!/usr/bin/python3
import psycopg2

conn = psycopg2.connect("host=192.168.56.30 dbname=project_db user=webuser1 password=student")

cursor = conn.cursor()


print("Content-type: text/html\n\n")
print("<html><head><title>Faculty Table</title>")
print("<style>")
print("table { width: 100%; border-collapse: collapse; }")
print("th, td { border: 1px solid black; padding: 8px; text-align: left; }")
print("th { background-color: #f2f2f2; }")
print("tr:nth-child(even) { background-color: #f9f9f9; }")
print("</style></head><body>")
print("<h1>Faculty Table</h1>")
print("PGSQL version:<br>")

cursor.execute("SELECT version();")
version = cursor.fetchone()
print("Result ", version[0])
print("<br>All rows from table faculty:<br>")

cursor.execute("SELECT * FROM faculty;")
faculty_records = cursor.fetchall()
print("<table>")
print("<tr><th>ID</th><th>Honorific</th><th>First Name</th><th>Middle Initial</th><th>Last Name</th><th>Email</th><th>Phone</th><th>Office</th><th>Research Interests</th><th>Rank</th><th>Remarks</th><th>Currently Employed</th></tr>")

for row in faculty_records:
    print("<tr>")
    for column in row:
        print(f"<td>{column}</td>")
    print("</tr>")
print("</table>")

cursor.close()
conn.close()
print("</body></html>")


