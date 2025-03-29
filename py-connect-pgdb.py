#!/usr/bin/python3
import psycopg2
import cgi

conn = psycopg2.connect("host=192.168.56.30 dbname=project_db user=webuser1 password=student")

cursor = conn.cursor()

class Faculty:
	def __init__(self, fid, honorific, first_name, middle_initial, last_name, email, phone, office, research_interests, rank, remarks, currently_employed):
		self.fid = fid
		self.honorific = honorific
		self.first_name = first_name
		self.middle_initial = middle_initial
		self.last_name = last_name
		self.email = email
		self.phone = phone
		self.office = office
		self.research_interests = research_interests
		self.rank = rank
		self.remarks = remarks
		self.currently_employed = currently_employed

	def html_row(self):
		return (f"<tr>"
			f"<td>{self.fid}</td>"
			f"<td>{self.honorific}</td>"
			f"<td>{self.first_name}</td>"
			f"<td>{self.middle_initial}</td>"
			f"<td>{self.last_name}</td>"
			f"<td>{self.email}</td>"
			f"<td>{self.phone}</td>"
			f"<td>{self.office}</td>"
			f"<td>{self.research_interests}</td>"
			f"<td>{self.rank}</td>"
			f"<td>{self.remarks}</td>"
			f"<td>{self.currently_employed}</td>"
			f"</tr>")

def html_faculty_output(faculty_list):
	table_html = "<table>"
	table_html += ("<tr>"
                   "<th>ID</th><th>Honorific</th><th>First Name</th><th>Middle Initial</th>"
                   "<th>Last Name</th><th>Email</th><th>Phone</th><th>Office</th>"
                   "<th>Research Interests</th><th>Rank</th><th>Remarks</th><th>Currently Employed</th>"
                   "</tr>")

	for faculty in faculty_list:
		table_html += faculty.html_row()
	table_html += "</table>"
	return table_html

def html_courses_output(courses_list):
    table_html = "<table>"
    table_html += ("<tr>"
                   "<th>Prefix</th><th>Number</th><th>Title</th><th>GU</th>"
                   "<th>CH</th><th>Frequency</th><th>Active</th><th>Description</th><th>Remarks</th>"
                   "</tr>")
    for course in courses_list:
        table_html += (f"<tr>"
                       f"<td>{course[0]}</td><td>{course[1]}</td><td>{course[2]}</td><td>{course[3]}</td>"
                       f"<td>{course[4]}</td><td>{course[5]}</td><td>{course[6]}</td><td>{course[7]}</td><td>{course[8]}</td>"
                       f"</tr>")
    table_html += "</table>"
    return table_html

def calculate_fte(prefix, ch, enrollment, gu):
    if prefix == "CSCI" and "G" in gu:
        return (ch * enrollment) / 186.23
    elif prefix == "CSCI" and "U" in gu:
        return (ch * enrollment) / 406.24
    elif prefix == "SENG" and "G" in gu:
        return (ch * enrollment) / 90.17
    elif prefix == "SENG" and "U" in gu:
        return (ch * enrollment) / 232.25
    elif prefix == "DASC":
        return (ch * enrollment) / 186.23
    else:
        return 0  # Default for unrecognized prefixes

def html_fte_output(fte_list):
    table_html = "<table>"
    table_html += ("<tr>"
                   "<th>Faculty</th><th>Year</th><th>Semester</th><th>FTE</th>"
                   "</tr>")
    for fte in fte_list:
        table_html += (f"<tr>"
                       f"<td>{fte['faculty']}</td><td>{fte['year']}</td>"
                       f"<td>{fte['semester']}</td><td>{fte['fte']}</td>"
                       f"</tr>")
    table_html += "</table>"
    return table_html

form = cgi.FieldStorage()
search_query = form.getvalue("search", "").strip()
tab = form.getvalue("tab", "faculty")
sort_name_query = form.getvalue("sort", "").strip()
sort_rank_query = form.getvalue("sort", "").strip()

print("Content-type: text/html\n\n")
print("<html><head><title>Faculty and courses</title>")
print("<style>")
print("table { width: 100%; border-collapse: collapse; }")
print("th, td { border: 1px solid black; padding: 8px; text-align: left; }")
print("th { background-color: #f2f2f2; }")
print("tr:nth-child(even) { background-color: #f9f9f9; }")
print("nav ul { display: flex; list-style-type: none; padding: 0; margin: 0; }")
print("nav ul li { margin-right: 20px; }")
print("nav ul li a { text-decoration: none; font-weight: bold; }")
print(".active { color: red; }")
print("</style></head><body>")
print('<nav>')
print('<ul>')
print(f'<li><a href="?tab=faculty" class="{ "active" if tab == "faculty" else "" }">Faculty</a></li>')
print(f'<li><a href="?tab=courses" class="{ "active" if tab == "courses" else "" }">Courses</a></li>')
print(f'<li><a href="?tab=fte" class="{ "active" if tab == "fte" else "" }">FTE</a></li>')
print('</ul>')
print('</nav>')

if tab == "faculty":
	print("<h1>Faculty Table</h1>")

	print('''
	<form method="get" action="">
		Search Faculty by Last Name: <input type="text" name="search" value="{0}">
		<input type="submit" value="Search">
		<button type="submit" name="sort" value="name">Sort Alphabetically by Last Name</button>
		<button type="submit" name="sort" value="rank">Sort Alphabetically by Rank</button>
		<input type="hidden" name="tab" value="faculty">
	</form>
	'''.format(search_query))


	if sort_name_query =="name":
		cursor.execute("SELECT * FROM faculty ORDER BY last_name ASC;")
	elif sort_rank_query == "rank":
		cursor.execute("SELECT * FROM faculty ORDER BY rank ASC;")
	elif search_query:
	    cursor.execute("SELECT * FROM faculty WHERE last_name ILIKE %s;", (f"%{search_query}%",))
	else:
	    cursor.execute("SELECT * FROM faculty;")
	records = cursor.fetchall()

	faculty_list = []

	for row in records:

	    faculty_obj = Faculty(
	        fid=row[0],
	        honorific=row[1],
	        first_name=row[2],
	        middle_initial=row[3],
	        last_name=row[4],
	        email=row[5],
	        phone=row[6],
	        office=row[7],
	        research_interests=row[8],
	        rank=row[9],
	        remarks=row[10],
	        currently_employed=row[11]
	    )
	    faculty_list.append(faculty_obj)


	print(html_faculty_output(faculty_list))

elif tab == "courses":
	print("<h1>Courses Table</h1>")
	try:
		cursor.execute("SELECT * FROM courses;")
		courses_records = cursor.fetchall()
	except Exception as e:
		print(f"<p>Error querying Courses table: {e}</p>")

	print(html_courses_output(courses_records))

elif tab == "fte":
	print("<h1>FTE Table</h1>")

	fte_list = []

	cursor.execute("SELECT id, first_name, last_name FROM faculty;")
	faculty_records = cursor.fetchall()


	for faculty in faculty_records:
		faculty_id = faculty[0]
		faculty_name = f"{faculty[1]} {faculty[2]}"


		cursor.execute("SELECT DISTINCT year, semester FROM course_schedule WHERE instructor = %s;", (faculty_id,))
		schedule_records = cursor.fetchall()

		for schedule in schedule_records:
			year = schedule[0]
			semester = schedule[1]


			cursor.execute("""
				SELECT cs.prefix, cs.enrollment, c.ch, c.gu
				FROM course_schedule AS cs
				LEFT JOIN courses AS c
				ON cs.prefix = c.prefix AND cs.number = c.number
				WHERE cs.year = %s AND cs.semester = %s AND cs.instructor = %s;
			""", (year, semester, faculty_id))
			course_records = cursor.fetchall()


			schedule_fte = 0
			for course in course_records:
				prefix = course[0]
				enrollment = course[1] or 0
				ch = course[2] or 0
				gu = course[3] or ""


				course_fte = calculate_fte(prefix, ch, enrollment, gu)
				schedule_fte += course_fte


			fte_list.append({
				"faculty": faculty_name,
				"year": year,
				"semester": semester,
				"fte": schedule_fte
			})

	print(html_fte_output(fte_list))





#    fte_list = []

#    cursor.execute("SELECT id, first_name, last_name FROM faculty;")
#    faculty_records = cursor.fetchall()

#    for faculty in faculty_records:
#        id = faculty[0]
#        faculty_name = f"{faculty[1]} {faculty[2]}"

#        cursor.execute("SELECT year, semester FROM course_schedule WHERE instructor = %s;", (id,))
#        schedule_records = cursor.fetchall()
#	cursor.execute(""" SELECT prefix, enrollment, ch, gu FROM courses JOIN course_schedule ON courses.course_id = course_schedule.course_id WHERE course_schedule.year = %s AND course_schedule.semester = %s AND course_schedule.faculty_id = %s; """, (year, semester, faculty_id))
#        course_records = cursor.fetchall()
	

#        for schedule in schedule_records:
#            year = schedule[0]
#            semester = schedule[1]

#	    cursor.execute(""" SELECT cs.prefix, cs.enrollment, c.ch, c.gu FROM course_schedule AS cs LEFT JOIN courses AS c ON cs.prefix = c.prefix AND cs.number = c.number WHERE cs.year = %s AND cs.semester = %s AND cs.instructor = %s; """, (year, semester, id))
#	    course_records = cursor.fetchall()


##            total_ch = 0
#            total_enrollment = 0
#            for course in course_records:
#                prefix = course[0]
##                enrollment = course[1]
 #               ch = course[2] or 0
#                gu = course[3] or ""
#                total_ch += ch
#                total_enrollment += enrollment

            # Calculate FTE
#	    if total_enrollment > 0:
#		fte = calculate_fte(prefix, total_ch, total_enrollment)
#	    else:
#		fte = 0
            # Append to FTE list
#            fte_list.append({
#                "faculty": faculty_name,
#                "year": year,
#                "semester": semester,
#                "fte": fte
#            })
   
#    print(html_fte_output(fte_list))



cursor.close()
conn.close()
print("</body></html>")



