import pypyodbc as odbc
import cgi, cgitb

citb.enable()

data = cgitb.FieldStorage()

output = data.getvalue("browser")

print "Content-Type: text/html\n"
print "the account_user_name is: " + data["account_user_name"].value
print "<br />"
print "the browser is: " + data["browser"].value
print "<br />"
print data

# {user_account_name: user_account_name, user_name: user_name, url: url, browser: browser})

# conn = odbc.connect("Driver=Microsoft Access Driver (*.mdb, *.accdb)};Dbq=\\eagle.usaa.com\usaa\cs\Facility\BUSINESS OPERATIONS ANALYTICS BOA\Sharepoint\corp_scv_traker.accdb;")

# cur = conn.cursor()

# sql = "insert into tblTraker(account_user_name, user_name, url) values(" + account_user_name + "," + user_name + "," + "url)"

# cur.execute(sql).commit()



